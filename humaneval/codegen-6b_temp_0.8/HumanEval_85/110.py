
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # lst[0], lst[1] = lst[1], lst[0]
    # lst[0], lst[2] = lst[2], lst[0]
    # lst[0], lst[3] = lst[3], lst[0]
    # lst[0], lst[4] = lst[4], lst[0]
    # lst[1], lst[2] = lst[2], lst[1]
    # lst[1], lst[3] = lst[3], lst[1]
    # lst[1], lst[4] = lst[4], lst[1]
    # lst[2], lst[3] = lst[3], lst[2]
    # lst[2], lst[4] = lst[4], lst[2]
    # lst[3], lst[4] = lst[4], lst[3]
    # return lst

    for i in range(0, len(lst), 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
