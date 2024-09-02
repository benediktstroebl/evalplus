
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    a=0
    b=0

    for i in range(len(lst)):
        if i%2==0 and lst[i]%2==0:
            a+=lst[i]
        elif i%2!=0 and lst[i]%2!=0:
            b+=lst[i]

    return a+b
