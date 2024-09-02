
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    x = []
    for index, item in enumerate(lst):
        if index % 2 == 0:
            if item % 2 == 0:
                x.append(item)
    return sum(x)

