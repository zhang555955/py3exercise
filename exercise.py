# _*_ coding:utf-8 _*_

__anthor__=u'橘子来了'
import sys
import math
import cmath
import random

if __name__=="__main__":
    seq_tuple=(1,2,3,4,5)
    seq_it=iter(seq_tuple)
    print("first:%s" % next(seq_it))
    print("first:%s" % next(seq_it))
    print("first:%s" % next(seq_it))

    print("\nfor循环遍历迭代器对像：")
    for_it=iter(seq_tuple)
    for x in for_it:
        print(x,end=" ")
    print("\n\nwhile & next遍历迭代器对象：")
    while_it=iter(seq_tuple)
    while True:
        try:
              print(next(while_it))
        except StopAsyncIteration:
              sys.exit()


'''
if __name__=="__main__":
    tuple_1=(1,2,3,4,5,6,7,8,9,0)
    list_1=[u"DeepTest",u"优测",u"Python3"]
    print(u"遍历元组，并打印出来：")
    for t in tuple_1:
        print(t,end=',')
    for l in list_1:
        print(l)



    var1=int(input(u"请输入一个整数："))
    if var1>=0 and var1<10:
        print(u"你输入一个大于0小于10的整数")
    elif var1>=10:
        print(u"你输入一个大于10的整数")
    else:
        print(u"你输入一个负数")

    print(u"set操作示例")
    set_soure=set([1,1,2,3,4,5,6,7])
    set_demo=set([1,1,2,3,4,5,6,7])
    print(u"原始数据：",end="")
    print(set_demo)
    # add方法，新增元素
    print(u"add后：",end="")
    set_demo.add(9)
    set_demo.add(1)
    print(set_demo)
    #remove 删除元素
    print(u"remove后：",end="")
    set_demo.remove(9)
    print(set_demo)
    #update新增多个元素值
    list_demo=["a","b","c"]
    set_demo.update(list_demo)

    print(u"update后：",end="")
    print(set_demo)



set1=set(u"DeepTest DeepTest")#这里体现了set的关键特性：无序、不重复。
print(set1)
    print(u"字典遍历、修改、删除示例")
    dict_demo={u"DeepTest":u"优测",u"ebook":u"快学Python3"}
    #遍历方法1
    for (key,value) in dict_demo.items():
        print("%s:%s"%(key,value))
    #遍历方法2
    for key in dict_demo.keys():
        print("%s:%s"%(key,dict_demo[key]))
        #字典的value可以存储任何类型Python对象，即可以是标准的类型，也可以是我们自定义的类型，但key不可以。
        # 字典的key是唯一的，不可以重复字典的key可以是数字、字符串甚至元组，但不可以用列表



    print(u"字典方法应用示例")
    dict_demo={u"DeepTest":u"优测",u"ebook":u"快学Python3"}
    tup1=[1,2,3,4]
    dict_cp=dict_demo.copy()#copy复制字典
    print(dict_demo)
    print(dict_cp)

    dict_new=dict.fromkeys(tup1,u"value")#以序列作为kye创建一个新字典，value为所有键对应的初始值
    print(dict_new)

    value1=dict_demo.get(u"DeepTest",u"我是默认值")#返回指定key的value，如果key不存在，则返回默认值
    value2=dict_demo.get(u"Python3",u"我是默认值")
    print(value1)
    print(value2)

    key=u"DeepTest"
    result1=key in dict_demo#判断key是否存在，是则返回True，否则返回False
    result2=key in dict_new
    print(result1)
    print(result2)

    items=dict_demo.items()#items, 以元组形式返回字典所有的(key, value),返回可遍历的的元组，元组的元素为(key,value)形式
    print(items)

    keys=dict_demo.keys()# keys 以列表形式返回字典所有的key
    print(keys)

    values=dict_demo.values()# values,返回字典中所有的value
    print(values)

    # setdefault, 如果key存在，则返回其对应的value，
    # 否则将该key和默认值插入到字典中，并返回默认值
    set_result1=dict_demo.setdefault(u"DeepTest",u"设置值")
    set_result2=dict_demo.setdefault(u"我是key",u"我是value")
    print(set_result1)
    print(set_result2)
    print(dict_demo)

    dict_demo.update(dict_new)# update, 更新字典
    print(dict_demo)






    dict={u"DeepTest":u"优测",u"book":u"快学python3"}
    print(len(dict))#计算字典长度

    str_d=str(dict)#以字符方式输入字典，将字典转换成字符窜
    print(str_d)
    print(dict)

    print(type(dict))#判断字典类型
    print(type(str_d))#字符窜str类型


    print(u"list方法代码：")
    list1=[1,1,2,2,2,3,3,3,4,5,6]
    list2=[7,8,9,0,10,11]

    list1.append(100)
    print(list1)
    count1=list1.count(2)
    print(count1)
    list1.extend(list2)
    print(list1)
    index=list1.index(2)
    print(index)
    list1.insert(0,200)
    print(list1)
    list1.pop()
    print(list1)
    list1.reverse()
    print(list1)
    list1.sort()
    print(list1)
    list3=list1.copy()
    print(list3)
    list1.clear()
    print(list1)
    print(list3)
    list3[-1]=500
    print(list3)


if __name__=="__main__":
    list_demo=[1,2,3,4,5,6]
    tuple1=tuple(list_demo)
    print(tuple1)
    print(u"link and join test!")
    tup1=(u"DeepTest",u"appium")
    tup2=(u"testingunion.com",u"hello",u"python3")
    tup4=(1,2,3,4)

    tup3=tup2+tup1
    tup5=tup1*2
    for t in tup4:
        print(t)

    #result=5 in tup4
    #print(result)
    print(len(tup4))
    print(tup5)
    print(tup1)
    print(tup2)
    del tup1
    print(tup3)

if __name__=="__main__":
    print(u"元组切片操作示例！")

    data_demo=(u"DeepTest",u"appium","testinggunion.com",u"hello",u"python3")
    e=data_demo[1]
    print(e)

    f=data_demo[-1]
    print(f)

    g=data_demo[1:]
    print(g)

    h=data_demo[1:4]
    print(h)


if __name__=="__main__":
    tuple_demo=(1,2,3,4,5,6,7,8,9,0)
    print(len(tuple_demo))
    print(max(tuple_demo))
    print(min(tuple_demo))

    list_demo=[1,2,3,4,5,6]
    tuple1=tuple(list_demo)
    print(tuple1)


if __name__=="__main__":
    str1="1234567890"
    str2="abcdefABCDEF"
    str3="12345abcdeABCDE"
    str4="abcdef"
    str5="ABCDEF"
    str6="      "
    str7="sfsdf"

    print(str3.isalnum(),"1")
    print(str2.isalpha(),"2")
    print(str1.isdigit(),"3")
    print(str4.islower(),"4")
    print(str2.islower(),"5")
    print(str4.isupper(),"6")
    print(str2.isupper(),"7")
    print(str6.isspace(),"8")
    print(str7.isspace(),"9")
    print(str1.isnumeric(),"10")
    print(str3.isnumeric(),"11")


if __name__=="__main__":
    source_str=u"it's my book,please show it,wa ka ka,yo yo yo!"

    print(u"left yo")
    print(source_str.find("qq"))
    print(source_str.index("yo"))

    print(u"right yo")
    print(source_str.rfind("yo"))
    print(source_str.rindex("yo"))

    print("rep")
    des_str=source_str.replace("yo","ha")
    print(des_str)

    print("rep 2")
    des_str=source_str.replace("yo","ha",2)
    print(des_str)

    demo_str="   我的前      后 和 中 间   都有空格   "
    print(demo_str)

    lstr=demo_str.lstrip()
    print(lstr)

    rstr=demo_str.rstrip()
    print(rstr)

    str=demo_str.strip()
    print(str)


if __name__=="__main__":
    t=('1','2','3','4','5','a','b','efg')

    str_demo='-'.join(t)
    print(str_demo)

    str_set=str_demo.split('-')
    print(str_set)

    str_demo=''.join(t)
    print(str_demo)

if __name__=="__main__":
    x=-100
    y=1.9
    print(u'常用数字函数')
    print(abs(x))#返回x的绝对值
    print(max(x,y))#返回最大值
    print(min(x,y))#返回最小值
    print(pow(y,2))#计算Y^2
    print(math.sqrt(y))#返回y的平方根
    print(u"常用随机函数")
    a=[1,2,3,4,5,6,7,8,9,0]
    print(random.choice(a))#从列表a中随机选中一个
    print(random.randrange(2,100,5))#从指定的2-100按5递增的数据集随机选中1个
    print(random.random())#生成一个随机数，它在（0，1）之间
    print(u"常用三角函数")
    x=100
    print(cmath.acos(x))#返X的返余弧度值
    print(cmath.sin(x))
    print(cmath.cos(x))
    print(u"数字常量")
    print(cmath.pi)#返回派



def outer(name):
    def inner("%s is %s:"(name,age):
    return inner
outer("why","18"))


if __name__=="__main__":
    print("参数 %d:" % len(sys.argv))
    print("参数 %s:" % len(sys.argv))
    print(dir(__builtins__))#查看所有内建函数

__author__='zhangjing'
if __name__ == "__main__":
    data=input"请输入一串任意字符：")
    list_data=data.split(' ')
    print(list_data)

    sum=0
    for index in range(1,100):
        sum=sum+index
    print("1-99的和为：%d" % sum)
'''


