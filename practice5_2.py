a = int(input())
b = int(input())
print("+ - * /")
op = input()

if op == "+":
    result = a+b
if op == "-":
    result = a-b
if op == "*":
    result = a*b
if op == "+":
    result = a/b
    if b == 0:
        result = "!!"
    else:
        result = a/b
else:
    print("Error!")
print(result)
