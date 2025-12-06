from PIL import Image
im=Image.open('generated.jpg')
im=im.resize((2048,1080), resample=Image.NEAREST)
im.save('generated2.jpg')