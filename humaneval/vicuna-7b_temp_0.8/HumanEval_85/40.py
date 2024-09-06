
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_index = [i for i, x in enumerate(lst) if x % 2 == 0]
    if len(even_index) > 0:
        for i in range(len(lst)):
            if i in even_index:
                lst[i], lst[len(even_index) - 1] = lst[len(even_index) - 1], lst[i]
                break
    return lst