
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    num=0
    for i in lst:
        if i%2==0 and i%2==1:
            num=num+i
    return num
