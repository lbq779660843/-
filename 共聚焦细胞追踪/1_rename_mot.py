import os
import numpy as np
import time

ori_path_lists = [r'D:\lbq\dataset\gjj\dataset\08_Tracking\CTMC-train\3T3-run01\img1',
                  r'D:\lbq\dataset\gjj\dataset\08_Tracking\CTMC-train\3T3-run03\img1',
                  r'D:\lbq\dataset\gjj\dataset\08_Tracking\CTMC-train\3T3-run05\img1',
                  r'D:\lbq\dataset\gjj\dataset\08_Tracking\CTMC-train\3T3-run07\img1',
                  r'D:\lbq\dataset\gjj\dataset\08_Tracking\CTMC-train\3T3-run09\img1',
]

ori_train_lists = [r'D:\lbq\dataset\gjj\dataset\08_Tracking\CTMC-train\3T3-run01\img1',
                  r'D:\lbq\dataset\gjj\dataset\08_Tracking\CTMC-train\3T3-run03\img1',
                  r'D:\lbq\dataset\gjj\dataset\08_Tracking\CTMC-train\3T3-run05\img1',
                  r'D:\lbq\dataset\gjj\dataset\08_Tracking\CTMC-train\3T3-run07\img1',]

ori_test_lists = [r'D:\lbq\dataset\gjj\dataset\08_Tracking\CTMC-train\3T3-run09\img1',]

voc_img_dir = r'D:\lbq\dataset\gjj\dataset\08_Tracking\JPEGImages'
voc_imgsets_dir = r'D:\lbq\dataset\gjj\dataset\08_Tracking\ImageSets\Main'

if not os.path.exists(voc_img_dir):
    os.makedirs(voc_img_dir)
if not os.path.exists(voc_imgsets_dir):
    os.makedirs(voc_imgsets_dir)


def img_rename_move(ori_path, new_path, fp):
    filelists = os.listdir(ori_path)  # 获取原路径下的所有图片列表
    for file in filelists:
        src = os.path.join(os.path.abspath(ori_path), file)  # 读取该文件的信息
        ori_name = os.path.basename(src)  # 读取该文件的文件名，不包含路径
        # print(ori_name)
        new_name = ori_path[-7:-5] + ori_name  # 将原文件名和文件夹名进行部分拼接，得到新的文件名
        txt_name = new_name[:-4]
        fp.write(txt_name + 'n')  # 将文件名去除后缀的部分以追加的形式写入txt文件
        # print(new_name)
        dst = os.path.join(os.path.abspath(new_path), new_name)
        os.rename(src, dst)


txt_train = voc_imgsets_dir + '/train.txt'
fp_train = open(txt_train, 'a+')
txt_test = voc_imgsets_dir + '/test.txt'
fp_test = open(txt_test, 'a+')

# img_rename_move(test_dir,test_outdir)
start_time = time.time()

for ori_path in ori_train_lists:
    print('this is processing {}'.format(str(ori_path)))
    img_rename_move(ori_path, voc_img_dir, fp_train)
fp_train.close()

for ori_path in ori_test_lists:
    print('this is processing {}'.format(str(ori_path)))
    img_rename_move(ori_path, voc_img_dir, fp_test)
fp_test.close()

end_time = time.time()
print('succeed , total cost {}'.format(end_time - start_time))
