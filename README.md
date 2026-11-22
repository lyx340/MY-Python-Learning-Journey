# My-Python-Learning-Journey

## 项目简介
本仓库用于存放我的 Python 课堂练习代码，练习基础语法、数据处理以及文件目录操作，记录学习过程，方便复盘和展示学习成果。

## 文件说明
- **dataFrame_01.py**：使用 pandas 构建 DataFrame，实现二维表格数据的创建与输出。
- **new.py**：调用 os 模块，批量自动创建子文件夹，练习文件路径操作。

## 代码说明
```python
# dataFrame_01.py
import pandas as pd
data = [[110,105,99],[105,88,106],[98,112,103]]
index = [0,1,2]
columns = ['语文','数学','英语']
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)

