
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    result = []
    for i in range(0, len(lst), 2):
        result.append(lst[i])
    return
