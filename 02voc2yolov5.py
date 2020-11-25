import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
sets = ['train', 'test','val']
classes = ['ship'] #需要更改
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)
def convert_annotation(image_id):
    in_file = open('Annotations/%s.xml' % (image_id)) #需要更改
    out_file = open('labels/%s.txt' % (image_id), 'w') #需要更改
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
wd = getcwd()
print(wd)
for image_set in sets:
    if not os.path.exists('labels/'):
        os.makedirs('labels/')
    image_ids = open('ImageSets/Main/%s.txt' % (image_set)).read().strip().split() #需要更改
    list_file = open('%s_sets_directory.txt' % (image_set), 'w')
    labels_list_file = open('%s_labels_directory.txt' % (image_set), 'w')
    for image_id in image_ids:
        print('i am working')
        list_file.write('images/%s.jpg\n' % (image_id))
        labels_list_file.write('labels/%s.txt\n' % (image_id))
        convert_annotation(image_id)
    list_file.close()
    labels_list_file.close()


