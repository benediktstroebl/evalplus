
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = sorted(lst)
    n = 0
    for i in range(len(lst)):
        if i % 2 == 1:
            n += lst[i]
        else:
            n += lst[i]
    result = [i for i in n]
    return result

lst = [3, 1, 5, 6, 2, 4, 9]
