import os
a = "/Users/luoyuxiu/Desktop/python/Python语言_10_目录及文件操作/Lesson_10_Path/sub"
for i in range(1,121):
    filename =f"sub{i:03d}"
    os.makedirs(os.path.join(a,filename),exist_ok = True)
    for n in range(1,11):
        filenamelast = f"Run{n:02d}"
        os.makedirs(os.path.join(a,filename,filenamelast),exist_ok = True)
print("文件夹创建完成！")
