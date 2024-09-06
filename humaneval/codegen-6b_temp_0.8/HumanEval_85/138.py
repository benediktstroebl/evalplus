
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    add_lst = []
    for i in range(0, len(lst), 2):
        add_lst.append(lst[i])
    return add_lst
