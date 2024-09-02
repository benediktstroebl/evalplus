
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    for i in range(1, len(lst), 2):
        lst[i] = lst[i] + lst[i-1]
    return lst
    
