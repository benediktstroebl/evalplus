
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    i = 0
    even_lst = []
    for x in lst:
        if x % 2 == 0:
            even_lst.append(x)
            i += 1
        else:
            lst[i] = even_lst[-1]
            i = 0
            even_lst = [x]
    lst[i] = even_lst[-1]
    return lst