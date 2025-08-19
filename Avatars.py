import python_avatars as pa
my_avatar = pa.Avatar(
    style=pa.AvatarStyle.CIRCLE,
    background_color=pa.BackgroundColor.WHITE,
    top=pa.HairType.SHORT_FLAT,
    eyebrows = pa.EyebrowType.DEFAULT_NATURAL,
    eyes = pa.EyeType.HAPPY,
    nose = pa.NoseType.DEFAULT,
    mouth = pa.MouthType.DEFAULT,
    facial_hair=pa.FacialHairType.NONE,
    skin_color= "#ffffff",
    hair_color=pa.HairColor.BLACK,
    accessory=pa.AccessoryType.ROUND,
    clothing=pa.ClothingType.BLAZER_SWEATER,
    clothing_color=pa.ClothingColor.PASTEL_BLUE)

my_avatar.render("my_avatar.svg")

print("Avatar created and saved as my_avatar.svg")
# The code creates an avatar using the python_avatars library and saves it as an SVG file.
# You can customize the avatar's features such as style, colors, and accessories.
# Make sure to have the python_avatars library installed in your environment.
    