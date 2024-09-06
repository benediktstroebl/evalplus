
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] > 0:
            lst[i], lst[i-2] = lst[i-2], lst[i]
    return lst

lst = [5, 6, 7, 2, 8, 9, 10]
