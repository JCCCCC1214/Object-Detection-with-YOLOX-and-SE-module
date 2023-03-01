import os

path_r = "ground_truth"
path_w = "groundtruths"
files = os.listdir(path_r)
files.sort(key =lambda x:int(x[:-4]))
for file in files:
    path_txt = path_r+"/"+file
    f_read = open(path_txt,'r')
    f_write = open(path_w+"/"+file,'w')
    for line in f_read:
        lines = line.split(' ')
        x = float(lines[1])
        y = float(lines[2])
        w = float(lines[3])
        h = float(lines[4])
        W = 1920
        H = 1080
        x1 = (x - w / 2) * W
        y1 = (y - h / 2) * H
        x2 = (x + w / 2) * W
        y2 = (y + h / 2) * H
        f_write.write(lines[0]+" "+str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2)+"\n")
    f_read.close()
    f_write.close()