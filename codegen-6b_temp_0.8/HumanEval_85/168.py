
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    
    temp = lst[0]
    for i in range(1, len(lst)):
        if i % 2 == 0:
            temp += lst[i]
    return temp


