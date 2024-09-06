
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    even_lst = [lst[0], lst[1], lst[-1]]
    for i in range(1, len(lst)):
        if lst[i] % 2 == 0:
            even_lst.append(lst[i])
            lst.remove(lst[i])
    return lst
