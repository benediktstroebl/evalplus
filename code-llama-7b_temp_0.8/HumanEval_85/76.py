
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # O(1) space
    # O(N) time
    return lst[1::2][::-1].sum()


