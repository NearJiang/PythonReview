>>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
>>> m
<_sre.SRE_Match object; span=(0, 9), match='010-12345'>
>>> m.group(0)
'010-12345'
>>> m.group(1)
'010'
>>> m.group(2)
'12345'

group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串

提取子串非常有用。来看一个更凶残的例子：

>>> t = '19:05:30'
>>> m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
>>> m.groups()#这边是 group s  多个s
('19', '05', '30')

0[0-9]表示可以匹配00-09
0[0-9]|1[0-9]|2[0-3]|[0-9]就表示可以是00-09或者10-19或者20-23或者0-9(兼容第一个
                                                         有的人写05，有人写5)
上面的是几点的正则表达式
