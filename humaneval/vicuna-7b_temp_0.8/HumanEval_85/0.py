
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    if not lst:
        return []
    even_lst = []
    odd_lst = lst[1:]
    for i, j in zip(lst, odd_lst):
        even_lst.append(j)
        odd_lst.append(i)
    return even_lst

