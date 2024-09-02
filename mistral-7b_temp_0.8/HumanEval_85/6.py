
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # TODO
    i = 0
    sum_lst = 0
    lst_len = len(lst)
    while i < lst_len:
        if lst[i] % 2 == 0 and i % 2 == 1:
            sum_lst += lst[i]
        i += 1

    return sum_lst

