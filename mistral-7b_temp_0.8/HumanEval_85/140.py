
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # add whatever you want to this list
    sum = 0
    i = 0
    while i < len(lst):
        if i % 2 != 0 and lst[i] % 2 == 0:
            sum += lst[i]
        i += 1
    return sum

