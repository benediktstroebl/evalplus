
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return []
    else:
        return [lst[i] if i % 2 != 0 else lst[i+1] for i in range(len(lst))]:

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
