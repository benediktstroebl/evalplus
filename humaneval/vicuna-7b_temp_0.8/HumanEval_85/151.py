
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return []
    return lst[1:len(lst)-1]

lst = [1, 2, 3, 4, 5]
result = add(lst)
