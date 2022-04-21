from exif import Image

img_path = '/Users/quentinikuta/Downloads/IMG_0491.jpg'

# Image without EX
with open (img_path, "rb") as src:
    img = Image(src)
if img.has_exif:
    info = (f" has the EXIF {img.exif_version}")
else:
    info = "does not contain any EXIF information"
print(f"Image {src.name}: {info}")

# Read again photo with exif info
with open(img_path, 'rb') as src:
    img = Image(src)
#print(img.list_all())
#print(img.gps_latitude, img.gps_latitude_ref)
#print(img.gps_longitude, img.gps_longitude_ref)

def decimal_coords(coords, ref):
    decimal_degrees = coords[0] + coords[1] / 60 + coords[2] / 3600
    if ref == 'S' or ref == 'W':
        decimal_degrees = -decimal_degrees
    return decimal_degrees

def image_coordinates(image_path):
    with open(img_path, 'rb') as src:
        img = Image(src)    
        if img.has_exif:
            try:
                img.gps_longitude
                coords = (decimal_coords(img.gps_latitude,img.gps_latitude_ref),decimal_coords(img.gps_longitude,img.gps_longitude_ref))
            except AttributeError:
                print ('No Coordinates')
        else:
            print ('The Image has no EXIF information')    
        print(f"Image {src.name}, OS Version:{img.get('software', 'Not Known')} ------")
        print(f"Was taken: {img.datetime_original}, and has coordinates:{coords}")

image_coordinates(img_path)

"""
future enhancements: 
- enhance to enter folder, iterate through all photos in that folder pulling coordinates, putting coordinates into spreadsheet
"""