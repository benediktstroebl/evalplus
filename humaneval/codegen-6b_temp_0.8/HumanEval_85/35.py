
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst[len(lst):len(lst):2] = [x+2 for x in lst[len(lst):len(lst):2]]
    return lst
