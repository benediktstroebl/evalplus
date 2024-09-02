
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    result = [0] * n
    i = 0
    while i < n - 1:
        if lst[i] % 2 == 0 and lst[i+1] % 2 != 0:
            result[i] = lst[i]
            i += 1
        else:
            result[i] = lst[i]
            i += 1
    return result

