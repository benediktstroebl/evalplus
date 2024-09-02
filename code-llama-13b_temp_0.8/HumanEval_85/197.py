
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    if not lst:
        return 0
    
    total = 0
    for index, number in enumerate(lst):
        if index % 2 == 1:
            if number % 2 == 0:
                total += number

    return total
