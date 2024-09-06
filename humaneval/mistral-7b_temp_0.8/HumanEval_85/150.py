
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    x=[]
    for i in range(1,len(lst)):
        if lst[i]%2==0:
            x.append(lst[i])

    return sum(x)
