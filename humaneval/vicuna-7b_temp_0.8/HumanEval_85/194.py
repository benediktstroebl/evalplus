
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_lst = [x for x in lst if x % 2 == 0]
    i = 0
    while i < len(even_lst) and lst[i] % 2 != 0:
        even_lst[i] += lst[i]
        i += 1
    return even_lst
