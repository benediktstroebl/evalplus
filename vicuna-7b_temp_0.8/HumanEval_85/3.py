
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    even_index = 0
    for i in range(n-1):
        if lst[i] % 2 == 0:
            even_index += 1
            lst[i], lst[even_index] = lst[even_index], lst[i]
    return lst