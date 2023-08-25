print("진수 변환기")
print('1번 : 10진수에서 타 진수로 변환\n2번 : 타 진수에서 10진수로 변환')
a = int(input('숫자를 입력하세요. : '))

if a == 1:

    print('10진수에서 어떤 진수로 변환하시겠습니까?')
    print('1번 : 2진수\n2번 : 8진수\n3번 : 16진수')
    b = int(input('숫자 입력 : '))

    if b == 1:
        bin_num = int(input('10진수 입력 : '))
        c = bin(bin_num)
        print('10진수', bin_num , '는 2진수로', c, '입니다.')

    elif b == 2:
        oct_num = int(input("10진수 입력 : "))
        c2 = oct(oct_num)
        print('10진수', oct_num,'는 8진수로', c2 , '입니다.')

    elif b == 3:
        hex_num = int(input("10진수 입력 : "))
        c3 = hex(hex_num)
        print('10진수', hex_num,'는 8진수로', c3, '입니다.')
        
    else:
        print('잘못된 선택 입니다.')
        exit()

if a == 2:

    print('어떤 진수를 10진수로 변환하시겠습니까?')
    print('1번 : 2진수\n2번 : 8진수\n3번 : 16진수')
    b2 = int(input('숫자 입력 : '))

    if b2 == 1:
        NumToBin = input('2진수 입력 : ')
        Dec_Num = int(NumToBin, 2)
        print('2진수', NumToBin , '는 10진수로', Dec_Num , '입니다.')

    elif b2 == 2:
        NumToOct = input("8진수 입력 : ")
        Dec_Num = int(NumToOct, 8)
        print('10진수', NumToOct,'는 8진수로', Dec_Num , '입니다.')

    elif b2 == 3:
        NumToHex = input("16진수 입력 : ")
        Dec_Num = int(NumToHex, 16)
        print('10진수', NumToHex,'는 8진수로', Dec_Num , '입니다.')

    else:
        print('잘못된 선택 입니다.')
        exit()