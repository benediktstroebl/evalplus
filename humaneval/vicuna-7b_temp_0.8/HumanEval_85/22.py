
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = list(lst)
    even_idx = [(i+1) // 2 for i in lst]
    lst = [(lst[i], lst[i+1]) for i in range(len(even_idx)-1)]
    lst = [x+y for x, y in lst if y % 2 == 0]
    return lst

