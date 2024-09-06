
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[idx] for idx, e in enumerate(lst) if e % 2 == 0 and idx % 2 == 1])
    
