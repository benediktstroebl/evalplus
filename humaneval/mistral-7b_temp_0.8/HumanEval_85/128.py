
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst_copy = lst.copy()
    for i in range(len(lst_copy)):
        if i % 2 != 0:
            if lst_copy[i] % 2 == 0:
                lst_copy[i] = lst_copy[i] + 1
                lst_copy[i - 1] = lst_copy[i - 1] + 1

    return lst_copy



