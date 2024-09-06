
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum(l for l, i in zip(lst, range(len(lst))) if i % 2 == 1 and l % 2 == 0)
