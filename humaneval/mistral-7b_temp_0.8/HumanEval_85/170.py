
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Check for the base cases
    if not lst:
        return 0

    # Find the first even element at an odd index
    for index, value in enumerate(lst):
        if value % 2 == 0 and index % 2 != 0:
            return value

    # If we reach here, there are no even elements at odd indices
    return 0
