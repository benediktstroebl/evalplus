
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    for i in range(len(lst)):
        if i%2==0:
            a=a+lst[i]
        else:
            b=b+lst[i]
    for i in range(len(lst)):
        if i%2==0:
            c=c+lst[i]
        else:
            d=d+lst[i]
    for i in range(len(lst)):
        if i%2==0:
            e=e+lst[i]
        else:
            f=f+lst[i]
    return a+b+c+d+e+f
