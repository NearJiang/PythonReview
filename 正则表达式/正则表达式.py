#正则表达式是一种用来匹配字符串的强有力的武器。
#它的设计思想是用一种描述性的语言来给字符串定义一个规则，
#凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的

#用\d可以匹配一个数字，'00\d'可以匹配'007'，但无法匹配'00A'/'\d\d\d'可以匹配'010'
#\w可以匹配一个字母或数字  '\w\w\d'可以匹配'py3'

# .可以匹配任意字符  'py.'可以匹配'pyc'、'pyo'、'py!'


用+表示至少一个字符，abc+:abc,abcc,abcccc (1到无限倍)
#用?表示0个或1个字符，abc？：ab，abc（0或1倍）
用{:n}表示,a{:2}b:b,ab,aab   a的0到n倍
#用*表示任意个字符（包括0个）,abc*:ab,abc,abcc,abccccc,abcccccccccc(0到无限倍)

用{n}表示n个字符：ab{2}c：abbc

用{n,m}表示n-m个字符，ab{1,2}c：abc,abbc

来看一个复杂的例子：\d{4}\s+\d{3,8}
\d{4}表示匹配4个数字，例如'0523'

\s可以匹配一个空格（也包括Tab等空白符），
   所以\s+表示至少有一个空格，例如匹配' '，' '等
\d{3,8}表示3-8个数字，例如'1234567'

综合，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码(0523 83489094) 

匹配中文：[\u4e00-\u9fa5]
