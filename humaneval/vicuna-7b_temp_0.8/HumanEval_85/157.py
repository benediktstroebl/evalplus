
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return lst
    i = 0
    while i < len(lst):
        if i % 2 == 1:
            j = i + 1
            while j < len(lst) and lst[j] % 2 == 0:
                j += 1
            lst[i:j+1] = [lst[i], lst[j]]
            i = j + 1
    return lst[i:]