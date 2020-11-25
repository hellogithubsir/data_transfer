import os
import shutil

# ------------------------------------------------------------------
# @function:将images和labels对应文件放入对应的train和valid下
# @autor:hongqing.wang
# @comment:
    #代码测试时通过的，如果出问题一般都是路径问题
# ------------------------------------------------------------------

#打印当前路径
wd = os.getcwd()
print(wd)

#取出对应文件放入对应文件
def get_picture_labels(object_directry, target_directoty):
    print('the direct is \" {} \"'.format(os.getcwd()))
    '''
    open & read content of the specific diretory
    '''
    with open(object_directry) as  f:  # mark1,根据输出的地址调节
        name_result = f.readlines()
        for i, str in enumerate(name_result):
            name_result[i] = (str.replace('\n', ''))
            # print('now  i is {},str is {}'.format(i , str)) #用于显示文件名或调试
            shutil.move(name_result[i], target_directoty)
            # shutil.copy(name_result[i], target_directoty)

    print((name_result))
    print('*********************************the type of name_result is {}*********************************'.format(type(name_result)))
    print('*********************************the trsnsfer is done*********************************')
    print('*********************************the trsnsfer is done*********************************')
    print('*********************************the trsnsfer is done*********************************')
    print('*********************************the trsnsfer is done*********************************')
    print('*********************************the trsnsfer is done*********************************')


def main():
    '''
    #transfer train pic
    '''
    object_directry = './train_sets_directory.txt'
    img_target_directoty = './my_datasets/train/images'
    get_picture_labels(object_directry, img_target_directoty)
    '''
    #transfer vaild pic
    '''
    object_directry = './test_sets_directory.txt'
    img_target_directoty = './my_datasets/valid/images'
    get_picture_labels(object_directry, img_target_directoty)
    '''
    #transfer train label
    '''
    object_directry = './train_labels_directory.txt'
    img_target_directoty = './my_datasets/train/labels'
    get_picture_labels(object_directry, img_target_directoty)
    '''
    #transfer valid label
     '''
    object_directry = './test_labels_directory.txt'
    img_target_directoty = './my_datasets/valid/labels'
    get_picture_labels(object_directry, img_target_directoty)


if __name__ == '__main__':
    main()
