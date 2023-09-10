import numpy as np, pandas as pd
from pulp import *
from ortoolpy import addvars, addbinvars
from io import StringIO

a = pd.read_table(StringIO("""\
曜日\t月\t月\t月\t火\t火\t火\t水\t水\t水\t木\t木\t木\t金\t金\t金\t土\t土\t土\t日\t日\t日
時間帯\t朝\t昼\t夜\t朝\t昼\t夜\t朝\t昼\t夜\t朝\t昼\t夜\t朝\t昼\t夜\t朝\t昼\t夜\t朝\t昼\t夜
必要人数\t2\t3\t3\t2\t3\t3\t2\t3\t3\t1\t2\t2\t2\t3\t3\t2\t4\t4\t2\t4\t4
従業員0\t○\t\t\t○\t\t\t○\t\t\t○\t\t\t○\t\t\t○\t\t\t○\t\t
従業員1\t○\t○\t○\t\t\t\t○\t○\t○\t\t\t\t○\t○\t○\t\t\t\t\t\t
従業員2\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t○\t○\t○\t○\t○\t○
従業員3\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○
従業員4\t\t\t○\t\t\t○\t\t\t○\t\t\t○\t\t\t○\t\t\t○\t\t\t○
従業員5\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t\t\t\t\t\t
従業員6\t\t\t\t\t\t\t\t\t\t\t\t\t○\t○\t○\t○\t○\t○\t○\t○\t○
従業員7\t\t○\t\t\t○\t\t\t○\t\t\t○\t\t\t○\t\t\t○\t\t\t○\t
従業員8\t\t\t○\t\t\t○\t\t\t○\t\t\t○\t\t\t○\t\t\t○\t\t\t○
従業員9\t\t\t\t\t\t\t\t\t\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○\t○""")).T
a,a.columns = a.iloc[1:],a.iloc[0].tolist()
a.必要人数 = a.必要人数.astype(int)
a.iloc[:,2:] = ~a.iloc[:,2:].isnull()
a.insert(0, '曜日', a.index.str[0])
a.reset_index(drop=True, inplace=True)
a = a.iloc[:,list(range(3,a.shape[1]))+[0,1,2]]
print(a[:3]) # 最初の3行表示