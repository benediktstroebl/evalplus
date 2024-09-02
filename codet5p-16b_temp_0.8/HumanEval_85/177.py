
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    l = [n for n in lst if not n % 2]
    lst = [n for n in lst if n % 2]

    return sum(lst) + sum(l)
