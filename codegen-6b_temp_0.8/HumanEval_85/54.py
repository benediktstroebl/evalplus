
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    ret = 0
    for i in lst:
        if i % 2 == 0:
            ret += i
    return ret

test = add([4, 2, 6, 7])
test = add([1, 2, 3, 4])
test = add([1, 2, 3, 4, 5])
test = add([1, 2, 3, 4, 5, 6])
