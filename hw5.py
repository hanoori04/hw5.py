num = input("세자리 정수 입력 : ")

def read_single_digit(number) :
    if number == "1" :
        return "일"
    if number == "2" :
        return "이"
    if number == "3" :
        return "삼"
    if number == "4" :
        return "사"
    if number == "5" :
        return "오"
    if number == "6" :
        return "육"
    if number == "7" :
        return "칠"
    if number == "8" :
        return "팔"
    if number == "9" :
        return "구"
    if number == "0" :
        return "영"
    
def read_Number(digit) :
    digit2 = digit.split

    if digit2[0] == "1" :
        return digit[0] == "일"
    if digit2[0] == "2" :
        return digit[0] == "이"
    if digit2[0] == "3" :
        return digit[0] == "삼"
    if digit2[0] == "4" :
        return digit[0] == "사"
    if digit2[0] == "5" :
        return digit[0] == "오"
    if digit2[0] == "6" :
        return digit[0] == "육"
    if digit2[0] == "7" :
        return digit[0] == "칠"
    if digit2[0] == "8" :
        return digit[0] == "팔"
    if digit2[0] == "9" :
        return digit[0] == "구"
    if digit2[1] == "1" :
        return digit[1] == "일"
    if digit2[1] == "2" :
        return digit[1] == "이"
    if digit2[1] == "3" :
        return digit[1] == "삼"
    if digit2[1] == "4" :
        return digit[1] == "사"
    if digit2[1] == "5" :
        return digit[1] == "오"
    if digit2[1] == "6" :
        return digit[1] == "육"
    if digit2[1] == "7" :
        return digit[1] == "칠"
    if digit2[1] == "8" :
        return digit[1] == "팔"
    if digit2[1] == "9" :
        return digit[1] == "구"
    if digit2[2] == "1" :
        return digit[2] == "일"
    if digit2[2] == "2" :
        return digit[2] == "이"
    if digit2[2] == "3" :
        return digit[2] == "삼"
    if digit2[2] == "4" :
        return digit[2] == "사"
    if digit2[2] == "5" :
        return digit[2] == "오"
    if digit2[2] == "6" :
        return digit[2] == "육"
    if digit2[2] == "7" :
        return digit[2] == "칠"
    if digit2[2] == "8" :
        return digit[2] == "팔"
    if digit2[2] == "9" :
        return digit[2] == "구"
    
if 0 <= int(num) <= 9:
    print(read_single_digit(num))

else :
    print(read_Number(num))
    