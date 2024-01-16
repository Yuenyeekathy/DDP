# print赋值
print("wzz is an idiot")
print("hello"+"world"+"!")

# 转义符\，忽略后面一位的符号
print("He said \"Let\'s go\"")

# \n换行符
print("Hello!\nHi")

# 三引号直接换行
print("""What are you talking about
Are you stupid
I'm pretty sure
Oh sorry""")

# 给变量赋值
my_love = "13428192813"
print("Please call " + my_love)

# 给原有变量重新赋值
greet = "你好，吃了吗您嘞,"
greet_chinese = greet
greet_english = "What's up bro,"
greet = greet_english
print(greet_chinese + "wzz")
print(greet + " Ultraman")

# 算一元二次方程平方根
a = -1
b = -2
c = 3
print((-b + (b**2 - 4 * a * c)**(1/2)) / (2 * a))
print((-b - (b**2 - 4 * a * c)**(1/2)) / (2 * a))

# 引入math公式计算
import math
a = -1
b = -2
c = 3
print((-b + math.sqrt(b**2 - 4 * a * c))/(2 * a))
print((-b - math.sqrt(b**2 - 4 * a * c))/(2 * a))

# 引入math公式计算其他
import math
print(math.sin(2))

# len计算字符串长度
print(len("wzz is an idiot"))

# type计算数据类型
print(type(None))

# []找出字符串的第几位值
commen_sense = "wzz is an idiot"
print(commen_sense[2])

# 计算用户的BMI BMI = 体重 / (身高 ** 2)
user_weight = float(input("Please input your weight(kg) :"))
user_height = float(input("Please input your height(m) :"))
user_BMI = str(user_weight / (user_height ** 2))
print("你的BMI值为：" + user_BMI)

# ==比较运算符
print("3" == "3")
print("a" == "b")

# !=不等于号
print("a" != "b")
print("3" != "3")

# 条件语句应用 what's wrong with this code?
mood_index = int(input("How does your girlfriend feel today?:"))
if mood_index >= 60:
    print("You can play games tonight!")
    print("Just enjoy!")
else:
    print("No game tonight!")
    print("Go shopping with her!")

# 条件嵌套,if和elif和else条件后都要加冒号
# 偏瘦：<=18.5
# 正常：18.5<BMI<=25
# 偏旁：25<BMI<=30
# 肥胖：>30
print("Here is the caculation of your BMI:")
user_weight = float(input("Please input your weight(kg) :"))
user_height = float(input("Please input your height(m) :"))
user_BMI = user_weight / (user_height ** 2)
print("你的BMI值为：" + str(user_BMI))
if user_BMI <= 18.5:
    print("此BMI值属于偏瘦范围")
elif 18.5 < user_BMI <= 25:
    print("此BMI值属于正常范围")
elif 25 < user_BMI <= 30:
    print("此BMI值属于偏胖范围")
else:
    print("此BMI值属于肥胖范围")

# 变大写
s = "hello"
print(s.upper())

s = "hello"
print(s)
s = s.upper()
print(s)

# 往列表里加/减元素
shopping_list = ["口红","眼影","腮红"]
shopping_list.append("粉底液")
shopping_list.remove("腮红")
print(shopping_list)

# 往列表里加各种类型的元素
shopping_list = ["口红"]
shopping_list.append(True)
shopping_list.append(33)
shopping_list.append(66.6)
print(shopping_list)

# 找到列表元素
shopping_list = ["口红","眼影","腮红"]
print(shopping_list[1])

# 修改列表元素
shopping_list = ["口红","眼影","腮红"]
shopping_list[0] = "粉底液"
print(shopping_list)
print(sorted(shopping_list))

# 数字列表
num_list = [3,8,-2.1,5.5,20,0]
print(max(num_list))
print(min(num_list))
print(sorted(num_list))
print(len(num_list))

# 查找字典里元素是否存在，往字典里加元素，减元素
contacts = {"wwy" : "17701959375",
            "wzz" : "13428192813",
            "lwx" : "13924902918"}
print("lwx" in contacts)
print("wqg" in contacts)
contacts["wqg"] = "13924923698"
print(contacts)
del contacts["wwy"]
print(contacts)

# 要多个值才能识别一个key，用tuple()
contacts = {("w","girl") : "17701959375",
            ("w","boy") : "13428192813"}
print(contacts[("w","boy")])

# 对字典执行迭代for
temperature_list = {"wwy" : 37.5, 
                    "wzz" : 36.8, 
                    "lwx" : 36.9, 
                    "wqg" : 37.2}
for name, temperature in temperature_list.items():
    if temperature > 37.3:
        print(name)

# range应用，不包含结束值，第三个值为步长
for i in range(1,5):
    print(i)
for i in range(1,5,2):
    print(i)

# 计算1到100相加的和
total = 0
for i in range(1,101):
    total = total + i
print(total)

# 拼合列表的每个元素
list1 = ["你","好","吗","兄","弟"]
print(range(len(list1)))
for element in list1:
    print(element)

for i in range(len(list1)):
    print(list1[i])

i = 0
while i < len(list1):
    print(list1[i])
    i = i + 1

# 对用户输入的数求平均值
print("Input several numbers and I will calculate the average for you")
user_input = input("Please input numbers(Please input E after the last number):")
total = 0
count = 0
while user_input != "E":
    num = float(user_input)
    total += num
    count += 1
    user_input = input("Please input numbers(Please input E after the last number):")
if count == 0:
    result = 0
else:
    result = total / count
print("The average of the numbers you input is:" + str(result))