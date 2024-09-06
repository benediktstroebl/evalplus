
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst_even_at_odd = [i for i in lst if i % 2 == 0 and i % 2 == 1]
    return sum(lst_even_at_odd)

