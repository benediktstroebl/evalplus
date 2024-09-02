
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # Your code here
    n = len(lst)
    if n == 0:
        return 0
    elif n == 1:
        return lst[0]
    else:
        return lst[1] + add(lst[2:])

