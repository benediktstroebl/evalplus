
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    i = 0
    while i < len(lst):
        if i % 2 == 0 and lst[i] % 2 == 0:
            i += 1
        elif lst[i] % 2 == 0 and i % 2!= 0:
            lst[i] = lst[i] + lst[i-1]
            i += 1
        else:
            i += 1
    return lst

