
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return []
    else:
        return [lst[0], lst[1], lst[1] % 2, lst[2] % 2]

lst = [3, 2, 6, 7, 4, 1, 5, 8]
print(add(lst))
