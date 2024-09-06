
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    result = []
    for i, num in enumerate(lst):
        if (i+1) % 2!= 0:
            result.append(num)

    return result

