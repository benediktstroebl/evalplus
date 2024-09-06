
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_idx = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            even_idx = i
    lst.insert(even_idx + 1, 2)
    return
