
from PIL import Image, ImageFilter
import math
import csv
lut=[]
   
def median_cut(color_list,depth):
    if(depth==1):
        sumr=0
        sumg=0
        sumb=0
        for i in color_list:
            r,g,b=i
            sumr+=r
            sumb+=b
            sumg+=g
        sumr=int(math.ceil(sumr/len(color_list)))
        sumg=int(math.ceil(sumg/len(color_list)))
        sumb=int(math.ceil(sumb/len(color_list)))
        lut.append((sumr,sumg,sumb))
        return 0


    red=[]
    blue=[]
    green=[]
    for i in color_list:
        r, g, b=i
        red.append(r)
        blue.append(b)
        green.append(g)
    diffr=max(red)-min(red)
    diffb=max(blue)-min(blue)
    diffg=max(green)-min(green)
    if(max(diffg,diffb,diffr)==diffr):
        color_list.sort(key=lambda x: x[0])
    elif(max(diffg,diffb,diffr)==diffb):
        color_list.sort(key=lambda x: x[1])
    else:
        color_list.sort(key=lambda x: x[2])
    mid=len(color_list)/2
    mid=int(mid)    
    median_cut(color_list[:mid],depth-1)
    median_cut(color_list[mid:],depth-1)


try:
    im = Image.open('peppers.tif')
    print ("The size of the Image is: ")
    print(im.format, im.size, im.mode)
    rgb_im = im.convert('RGB')

    width, height = im.size
    image_color=[]

    for i in range(1,width):
        for j in range(1,height):
            image_color.append(rgb_im.getpixel((i, j)))
    dep=9
    median_cut(image_color,dep)
    print("Hello")


   
    with open('palette.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["index","red pixel", "blue pixel","green pixel"])
        for i in range(256):
             writer.writerow([i,lut[i][0],lut[i][1],lut[i][2]])
             
             


except:
    print ("Unable to load image")