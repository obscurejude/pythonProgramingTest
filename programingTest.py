#judgeAでAの回答を判断する。A, B, Cは同じく、他の二人のカードが「1,5」「1,2」「4,5」の場合、即判断できる。
#それ以外の場合「わからない」となる
#戻り値：ゲーム継続ならtrue, ゲーム中止ならflase

def judgeA(B, C):
    if((B==1 and C==5) or (B==5 and C==1)):
        print("A->Mid")
        return False
    elif((B==4 and C==5) or (B==5 and C==4)):
        print("A->Min")
        return False
    elif((B==1 and C==2) or (B==2 and C==1)):
        print("A->Max")
        return False
    else:
        print("A->Unknown")
        return True

#judgeBでAがわからない前提でBの解答を判断する。
#Aと同じく他の二人のカードが「1,5」「1,2」「4,5」の場合（即判断条件）、即判断できる。
#Aがわからないと回答したため、Cが1,2,4,5の場合、それぞれBは自分が[2 or 5], [1], [5],[1 or 4]でないことを判断できる。さらにAのカードを元に自分が何のカードを持つかを判断できる場合がある
#戻り値：ゲーム継続ならtrue, ゲーム中止ならflase

def judgeB(A,C):
    if((A==1 and C==5) or (A==5 and C==1)):
        print("B->Mid")
        return False
    elif((A==4 and C==5) or (A==5 and C==4)):
        print("B->Min")
        return False
    elif((A==1 and C==2) or (A==2 and C==1)):
        print("B->Max")
        return False
    elif(C==1): #この場合、B!=2 and B!=5と判断できる。
        if(A==3):
            print("B->Max")
            return False
        elif(A==4):
            print("B->Mid")
            return False
    elif(C==2): #この場合、B!=1と判断できる。
        if(A==3):
            print("B->Max")
            return False
        elif(A==5):
            print("B->Mid")
            return False
        elif(A==4):
            print("B->Unknown")
            return True
    elif(C==4): #この場合、B!=5と判断できる。
        if(A==3):
            print("B->Min")
            return False
        elif(A==1):
            print("B->Mid")
            return False
        elif(A==2):
            print("B->Unknown")
            return True
    elif(C==5): #この場合、B!=1 and B!=4と判断できる。
        if(A==3):
            print("B->Min")
            return False
        elif(A==2):
            print("B->Mid")
            return False
    else:
        print("B->Unknown")
        return True

    
#judgeCでA, Bがわからない前提でCの解答を判断する。
#A, Bがわからない場合、以下のパターンしかない
#A=4, B=3 or 5 この場合、C=2と判断でき、Cの回答が「min」(47行参照)
#A=2, B=1 or 3この場合、C=4と判断でき、Cの回答が「max」(57行参照)
#以上以外場合、C=3と判断でき、Cの回答はAとBを見て判断する
#戻り値：ゲーム継続ならtrue, ゲーム中止ならflase

def judgeC(A,B):
    if(A==4 and (B==3 or B==5)):
        print("C->Min")
        return False
    elif(A==2 and (B==1 or B==3)):
        print("C->Max")
        return False
    elif((A>3 and B<3) or (A<3 and B>3)):
        print("C->Mid")
        return False
    elif(A>3 and B>3):
        print("C->Min")
        return False
    else:
        print("C->Max")
        return False
    
checkNGFlag=True #A, B, Cの入力チェック, OKの場合はFlase, NGの場合はTrue
while(checkNGFlag):
    print("Please input A:")
    A = int(input())
    print("Please input B:")
    B = int(input())
    print("Please input C:")
    C = int(input())
    if(A==B or B==C or A==C):
        print("Error: A,B,C should be different values. Input again:")
        checkNGFlag=True
    elif(int(A)>5 or int(B)>5 or int(C)>5):
        print("Error: A,B,C out of range. Input again:")
        checkNGFlag=True
    else:
        checkNGFlag=False

while(judgeA(B,C)):
    while(judgeB(A,C)):
        result=judgeC(A,B)
        break
    break
