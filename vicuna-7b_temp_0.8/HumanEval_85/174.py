
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    n = len(lst)
    if n % 2 == 0:
        return lst
    i = 0
    while i < n//2:
        j = i + 1
        if j >= n or lst[j] % 2 == 0:
            break
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
    return lst