
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    summ = 0
    for i in range(1, len(lst), 2):
        summ += lst[i]
    return summ

