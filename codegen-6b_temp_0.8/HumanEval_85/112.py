
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    for ind, e in enumerate(lst):
        if ind % 2 == 0 and e % 2 != 0:
            yield e

add([4, 2, 6, 7])
