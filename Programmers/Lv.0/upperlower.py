str = ""

for i in input():
    str += i.upper() if i.islower() else i.lower()

print(str) 

# 가장 효율적인 코드 print(input().swapcase())