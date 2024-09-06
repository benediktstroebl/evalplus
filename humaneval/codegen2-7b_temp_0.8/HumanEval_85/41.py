
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    odd, even = 0, []
    for val in lst:
        if not odd % 2:
            even.append(val)
        odd += 1

    return even
