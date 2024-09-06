
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    if not lst:
        raise ValueError("List can not be empty")

    # The first even element is at odd indices so add it to the sum
    if not lst[0] % 2:
        sum_ = lst[0]
    else:
        sum_ = 0
    for index in range(1, len(lst)):
        if lst[index] % 2:
            sum_ += lst[index]
    return sum_
