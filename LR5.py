def func(par2, par3):
    result =0
    m=par3*par3
    y=0
    f=0

    if m < 359 and par2 ==True:
        y=m*50
    else:

        if par2==True and m>30:
            y=m*100
        else: return result
    while f < y :
        result=result+f
        f+=1
    return result
    
print(func(True,3))
print(func(True,33))
print(func(True,333))
print(func(False,3))
print(func(False,33))
print(func(False,333))