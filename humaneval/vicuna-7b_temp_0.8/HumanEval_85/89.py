
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # sort the list to ensure the added element is at the correct index
    lst = sorted(lst)
    even = 0
    i = 0
    while i < len(lst) - 1:
        if lst[i] % 2 == 0:
            even += lst[i]
            lst[i], lst[i+1] = lst[i+1], lst[i]
            i += 1
        i += 1
    return lst