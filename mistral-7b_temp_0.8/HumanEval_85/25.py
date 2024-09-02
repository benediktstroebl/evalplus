
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Write your code here
    if not lst:
        raise TypeError("Empty list")

    return sum([v for i, v in enumerate(lst) if i % 2 != 0 and v % 2 == 0])
