
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    s = [lst[0]]
    for i in range(1, len(lst)):
        if not(lst[i] % 2):
            s.append(s[-1]+lst[i])
        else:
            s.append(lst[i])
    return s