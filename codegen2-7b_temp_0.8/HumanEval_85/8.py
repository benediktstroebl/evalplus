
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    for i, _ in enumerate(lst):
        if i % 2 == 1:
            lst[i] += 1
            
    return
