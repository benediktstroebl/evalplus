
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return [lst[i] + lst[i+1] for i in range(0, len(lst)-1, 2)
