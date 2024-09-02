
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    odd_index = True
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            if odd_index:
                odd_index = False
                continue
            else:
                return lst[i]
    if odd_index:
        return 0
    else:
        return lst[-1]



