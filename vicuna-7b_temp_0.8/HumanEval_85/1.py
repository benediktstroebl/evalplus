
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_index = [i for i, x in enumerate(lst) if x % 2 == 0]
    lst.extend(even_index)
    return lst
