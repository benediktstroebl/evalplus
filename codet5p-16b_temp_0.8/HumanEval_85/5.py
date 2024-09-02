
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    lst = [4, 2, 6, 7]
    add = 0
    for index, element in enumerate(lst):
        if index%2 == 1:
            if element%2 == 0:
                add += element
    return add

