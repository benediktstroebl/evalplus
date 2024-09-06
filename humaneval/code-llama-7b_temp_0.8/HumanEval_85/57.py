
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # check list is not empty
    if len(lst) == 0:
        return 0

    # check list is not empty
    if len(lst) == 1:
        return lst[0]

    # Traverse the list from odd position
    new_lst = [e for i, e in enumerate(lst) if i % 2 == 1]
    return sum(new_lst)

