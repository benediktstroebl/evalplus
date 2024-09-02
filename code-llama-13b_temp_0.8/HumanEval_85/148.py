
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return 0

    sum_ = 0

    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            sum_ += lst[i]

    return sum_

