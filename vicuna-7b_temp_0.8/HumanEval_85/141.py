
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # sort the elements of the list
    lst = sorted(lst)
    # if the list is empty, return an empty list
    if not lst:
        return []
    # if the list is empty, return an empty list
    if not lst:
        return []
    # return the even elements that are at odd indices
    return [lst[0], lst[1] if lst[1] else lst[0]]
