long_text= """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""


final={}              #新建新格式
sub_fund=[]           #新建次级格式
number=3              #行的记号
k=long_text.count("\n")

final["name"]=long_text.splitlines()[1]
final["lei"]=long_text.splitlines()[2]

while True:
    this_fund={}
    if number+1>k:
        break
    this_fund["title"] = long_text.splitlines()[number][3:]
    number+=1
    those_isin=[]
    while True:
        if long_text.splitlines()[number][0]=="L":
            those_isin.append(long_text.splitlines()[number])
            number+=1
        if number+1>k:
            break
        if long_text.splitlines()[number][0] != "L":
            break
    this_fund["isin"]=those_isin
    sub_fund.append(this_fund)
    if not long_text:
        break






final["sub_fund"]=sub_fund

print(final)

