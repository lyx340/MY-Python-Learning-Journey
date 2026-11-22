# My-Python-Learning-Journey

## 项目简介
本仓库用于存放我的 Python 课堂练习代码，练习基础语法、数据处理以及文件目录操作，记录学习过程，方便复盘和展示学习成果。

## 文件说明
- **dataFrame_01.py**：使用 pandas 构建 DataFrame，实现二维表格数据的创建与输出。
- **new.py**：调用 os 模块，批量自动创建子文件夹，练习文件路径操作。

## 代码说明
```python
# dataFrame_01.py
# 导入 pandas 数据分析库，简写为 pd 方便调用
import pandas as pd

# 定义原始数据：3行分别对应3名学生的语数英成绩
data = [[110,105,99],[105,88,106],[98,112,103]]
# 定义行索引，对应表格的行编号
index = [0,1,2]
# 定义列名，对应表格的科目名称
columns = ['语文','数学','英语']

# 核心语句：将数据、行索引、列名整合为 DataFrame 二维表格对象
df = pd.DataFrame(data=data, index=index, columns=columns)
# 打印输出最终表格结果
print(df)


# new.py
# 导入 os 模块，用于操作电脑文件与目录
import os

# 定义根目录绝对路径，所有文件夹都将创建在此路径下
a = "/Users/luoyuxiu/Desktop/python/Python语言_10_目录及文件操作/Lesson_10_Path/sub_new"

# 外层循环：创建 120 个一级子文件夹 sub001 ~ sub120
for i in range(1,121):
    # 格式化生成文件夹名称，补零对齐保证排序整齐
    filename =f"sub{i:03d}"
    # 拼接根路径与文件夹名，生成完整目录路径
    os.makedirs(os.path.join(a,filename),exist_ok = True)
    
    # 内层循环：在每个一级文件夹内，创建 10 个二级文件夹 Run01 ~ Run10
    for n in range(1,11):
        filenamelast = f"Run{n:02d}"
        # 拼接两级路径，创建二级子目录
        os.makedirs(os.path.join(a,filename,filenamelast),exist_ok = True)

# 程序执行完成后输出提示
print("文件夹创建完成！")
```
## 学习心得与规划
  在完成本次任务的过程中，我主动浏览了 GitHub 上大量优秀的 Python 学习项目，同时借助 B 站、小红书等平台查找学习教程、参考他人的学习经验和代码写法。通过观摩别人完整、规范的项目整理方式，我深刻意识到：写代码不仅要能运行，更要有清晰的文档、规范的提交记录和完整的项目说明，这既是学习习惯，也是展现个人学习能力的重要方式。以往我只会单纯写代码，不会整理项目、复盘知识点。经过本次作业，我学会了管理个人代码仓库、撰写项目说明、记录学习过程。未来我会持续使用 GitHub 仓库记录 Python 学习内容，每次练习后及时提交代码、总结易错点和学习收获，不断参考优秀项目优化自己的代码风格，养成复盘、积累、规范管理项目的好习惯，让仓库成为自己持续成长的学习档案。
