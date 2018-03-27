# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 20:00:01 2018

@author: 紫盛
"""
import glob
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import scipy.io
import scipy.misc


#src_txt_dir = r'text_original'
#src_txt_chinese = 'chinese.txt'
#src_txt_english = 'english.txt'

src_image_dir = r'images'
src_boxes_dir = r'texts'

##src_txt_dir = r"E:/ICPR/dataT_9000"
##src_xml_dir = r"E:/ICPR/dataX_9000"

image_Lists = glob.glob(src_image_dir + '/*.jpg')

img_basenames = [] # e.g. 100.txt

for img in image_Lists:
    img_basenames.append(os.path.basename(img))

img_names = [] # e.g. 100
for item in img_basenames:
    temp1, temp2 = os.path.splitext(item)
    img_names.append(temp1)
    
    for img in img_names:
# open the crospronding txt file
#gt = open(src_txt_dir + '/gt_' + img + '.txt').read().splitlines()
        
        #read_text_name = src_boxes_dir + '/' + img +　'.txt'
        #image = scipy.misc.imread(src_image_dir + '/' + img + '.jpg')

        image_input = Image.open(src_image_dir + '/' + img + '.jpg')        
        image = np.array(image_input,dtype='float32')
        #image = np.expand_dims(image, 0)  # Add batch dimension.       
        #image = mpimg.imread(src_image_dir + '/' + img + '.jpg')
        
        print (type(image))
        print('size is :',image.shape)
        thickness = (image.shape[0] + image.shape[1]) // 300
        #output_image = plt.imread(src_image_dir + '/' + img + '.jpg')
        #imshow(output_image)
        gt = open(src_boxes_dir + '/' + img + '.txt').read().splitlines()
        
        for txt_each_label in gt:
            #spt = txt_each_label.strip().split(',')
            boxes = np.array(txt_each_label.strip().split(',')[0:8]).astype('int32')
            label = txt_each_label.strip().split(',')[8]
            print(boxes)
            draw = ImageDraw.Draw(image_input)
            label_size = draw.textsize(label)#, font)
            
            x = np.minimum(image.shape[1],np.maximum(0,boxes[::2]))
            y = np.minimum(image.shape[0],np.maximum(0,boxes[1::2]))
            x1,x2,x3,x4 =  x 
            y1,y2,y3,y4 = y
            
            for i in range(thickness):
                draw.polygon([x1+i,y1+i,x2+i,y2-i,x3-i,y3-i,x4-i,y4+i],outline='red')
                            

    image_input.show()     
    image_input.save(os.path.join(img+'.jpg'), quality=90)
            
   