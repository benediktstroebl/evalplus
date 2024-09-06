
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return []
    n = len(lst)
    evens = [lst[i] for i in range(n // 2) if not lst[i] % 2]
    lst = [lst[i] for i in range(n) if i % 2 == 0]
    return lst + evens

