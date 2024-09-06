
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    even_odd_lst = []
    for i in lst:
        if i % 2 == 0:
            even_odd_lst.append(i)
        if i % 2 == 1:
            even_odd_lst.append(i)
    return even_odd_lst
