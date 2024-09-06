
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    temp = lst[0]
    j = 1
    for i in range(1, len(lst)):
        if not lst[j] % 2:
            temp += lst[j]
        j += 1
    return temp
    