
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    i = 0
    while i < len(lst)-1:
        if (lst[i] % 2 == 0) and (lst[i+1] % 2 == 0):
            lst[i], lst[i+1] = lst[i+1], lst[i]
            i += 1
    return lst

lst = [2, 6, 3, 8, 2, 9, 5, 1, 7]
