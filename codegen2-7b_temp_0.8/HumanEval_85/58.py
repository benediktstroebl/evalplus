
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst_len = len(lst)
    result = []
    for i in range(0, lst_len, 2):
        result.append(lst[i])
    return result
