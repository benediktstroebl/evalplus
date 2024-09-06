
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    i = 0
    while i < len(lst) - 1:
        if lst[i] % 2 == 0:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            i += 1

lst = [2, 3, 1, 4, 5, 6, 7, 8, 9]
