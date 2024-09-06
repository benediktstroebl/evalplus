
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = [x for x in lst if x % 2 == 0]
    remaining_lst = [x for x in lst if x % 2 == 1]
    for i in range(0, len(remaining_lst), 2):
        lst.insert(i, remaining_lst[i])
    return lst
