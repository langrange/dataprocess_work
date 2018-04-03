# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 16:00:02 2018

@author: qxb-810
"""

# -*- coding: utf-8 -*-
import io  
import re
import os, sys
import glob
from PIL import Image
from operator import itemgetter 
import numpy as np

#src_txt_dir = r'text_original'
#src_txt_chinese = 'chinese.txt'
#src_txt_english = 'english.txt'

src_txt_dir = r'text_temp'
src_txt_chinese = 'chinese_temp.txt'
src_txt_english = 'english_temp.txt'

##src_txt_dir = r"E:/ICPR/dataT_9000"
##src_xml_dir = r"E:/ICPR/dataX_9000"

txt_Lists = glob.glob(src_txt_dir + '/*.txt')

txt_basenames = [] # e.g. 100.txt

for txt in txt_Lists:
    txt_basenames.append(os.path.basename(txt))

txt_names = [] # e.g. 100
for item in txt_basenames:
    temp1, temp2 = os.path.splitext(item)
    txt_names.append(temp1)

def is_chinese(uchar):
        """判断一个unicode是否是汉字"""
        if uchar >= u'\u4E00' and uchar <= u'\u9FA5':
            return True
        else:
            return False

def divide2ChineseorEnglish(strpp,dict_chinese,dict_english):
   
    ustr = strpp.decode("UTF-8")
    for uchar in ustr:
        if is_chinese(uchar):
            
            if dict_chinese.has_key(uchar):
                dict_chinese[uchar] +=1
            else:
                dict_chinese[uchar] =1
        else:
            
            if dict_english.has_key(uchar):
                dict_english[uchar] +=1
            else:
                dict_english[uchar] =1
                    
dict_chinese ={} 
dict_english ={} 

print txt_names

for txt in txt_names:
# open the crospronding txt file
#gt = open(src_txt_dir + '/gt_' + img + '.txt').read().splitlines()
    gt = open(src_txt_dir + '/' + txt + '.txt').read().splitlines()
    
    for txt_each_label in gt:
        spt = txt_each_label.strip().split(',')
        spt
        divide2ChineseorEnglish(spt[8],dict_chinese,dict_english)

dict_chinese =sorted(dict_chinese.items(), key=itemgetter(1), reverse=True) 
dict_english =sorted(dict_english.items(), key=itemgetter(1), reverse=True) 

#list_chinese = dict_chinese.keys()
#list_english = dict_english.keys()

print dict_chinese

fwrite_chinese = io.open(src_txt_chinese,'w',encoding = 'utf-8')
for k in dict_chinese:
    fwrite_chinese.write(k[0] + '\t' + repr(k[1]) + '\n')
fwrite_chinese.close()

fwrite_english = io.open(src_txt_english,'w',encoding = 'utf-8')
for k in dict_english:
    print k
    fwrite_english.write(k[0] + '\t' + repr(k[1]) + '\n')
fwrite_english.close()
