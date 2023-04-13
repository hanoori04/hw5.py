# 202310992 컴퓨터과학과 하누리 과제제출

num = input("세자리 정수 입력 : ")

if len(num) == 1 :

    def read_single_digit(digit) : # 한자리 정수 한글 반환 함수
        if digit == "1" :
            return "일"
        if digit == "2" :
            return "이"
        if digit == "3" :
            return "삼"
        if digit == "4" :
            return "사"
        if digit == "5" :
            return "오"
        if digit == "6" :
            return "육"
        if digit == "7" :
            return "칠"
        if digit == "8" :
            return "팔"
        if digit == "9" :
            return "구"
        if digit == "0" :
            return "영"
        
    read_single_digit(num)

    print(read_single_digit(num))

elif len(num) == 2 :

    def read_second(second) : # 조건엔 없지만 추가로 두자리 정수 한글 반환 함수

        numnu = list(second)
        numnu2 = []

        if numnu[0] == "1" :
            numnu2.append("일")
    
        if numnu[0] == "2" :
            numnu2.append("이")

        if numnu[0] == "3" :
            numnu2.append("삼")

        if numnu[0] == "4" :
            numnu2.append("사")

        if numnu[0] == "5" :
            numnu2.append("오")

        if numnu[0] == "6" :
            numnu2.append("육")

        if numnu[0] == "7" :
            numnu2.append("칠")

        if numnu[0] == "8" :
            numnu2.append("팔")

        if numnu[0] == "9" :
            numnu2.append("구")

        if numnu[1] == "1" :
            numnu2.append("일")

        if numnu[1] == "2" :
            numnu2.append("이")

        if numnu[1] == "3" :
            numnu2.append("삼")

        if numnu[1] == "4" :
            numnu2.append("사")

        if numnu[1] == "5" :
            numnu2.append("오")

        if numnu[1] == "6" :
            numnu2.append("육")

        if numnu[1] == "7" :
            numnu2.append("칠")

        if numnu[1] == "8" :
            numnu2.append("팔")

        if numnu[1] == "9" :
            numnu2.append("구")

        if numnu[1] == "0" :
            numnu2.append("영")

        return numnu2
    
    d = read_second(num)[0]
    f = read_second(num)[1]

    print(d,f)
    

else :    
    def read_number(number) : # 세자리 정수 한글 반환 함수

        numnum = list(number)
        numnum2 = []

        if numnum[0] == "1" :
            numnum2.append("일")
    
        if numnum[0] == "2" :
            numnum2.append("이")

        if numnum[0] == "3" :
            numnum2.append("삼")

        if numnum[0] == "4" :
            numnum2.append("사")

        if numnum[0] == "5" :
            numnum2.append("오")

        if numnum[0] == "6" :
            numnum2.append("육")

        if numnum[0] == "7" :
            numnum2.append("칠")

        if numnum[0] == "8" :
            numnum2.append("팔")

        if numnum[0] == "9" :
            numnum2.append("구")

        if numnum[1] == "1" :
            numnum2.append("일")

        if numnum[1] == "2" :
            numnum2.append("이")

        if numnum[1] == "3" :
            numnum2.append("삼")

        if numnum[1] == "4" :
            numnum2.append("사")

        if numnum[1] == "5" :
            numnum2.append("오")

        if numnum[1] == "6" :
            numnum2.append("육")

        if numnum[1] == "7" :
            numnum2.append("칠")

        if numnum[1] == "8" :
            numnum2.append("팔")

        if numnum[1] == "9" :
            numnum2.append("구")

        if numnum[1] == "0" :
            numnum2.append("영")
    
        if numnum[2] == "1" :
             numnum2.append("일")

        if numnum[2] == "2" :
            numnum2.append("이")

        if numnum[2] == "3" :
            numnum2.append("삼")

        if numnum[2] == "4" :
            numnum2.append("사")

        if numnum[2] == "5" :
            numnum2.append("오")

        if numnum[2] == "6" :
            numnum2.append("육")

        if numnum[2] == "7" :
            numnum2.append("칠")

        if numnum[2] == "8" :
            numnum2.append("팔")

        if numnum[2] == "9" :
            numnum2.append("구")

        if numnum[2] == "0" :
            numnum2.append("영")

        return numnum2 
    
    a = read_number(num)[0]  
    b = read_number(num)[1]  
    c = read_number(num)[2]  
    print(a,b,c)





    

    
       




    
    





    
    



        

    
    


   


