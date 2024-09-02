
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    if not lst:
        raise ValueError('You gave me an empty list!')

    add_result = []
    for i in range(len(lst)):
        if i%2 != 0:
            if lst[i] % 2 == 0:
                add_result.append(lst[i])

    return sum(add_result)
