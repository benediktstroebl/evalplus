
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst_even = list(filter(lambda x: x % 2 == 0, lst))
    lst_odd = list(filter(lambda x: x % 2!= 0, lst))
    summ = sum(lst_even)
    for index, x in enumerate(lst_odd):
        summ += x
    return summ

