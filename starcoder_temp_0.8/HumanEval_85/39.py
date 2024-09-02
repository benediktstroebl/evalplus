
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    for index, x in enumerate(lst):
        if index % 2!= 0:
            if x % 2 == 0:
                lst[index] += x
    return sum(lst)

