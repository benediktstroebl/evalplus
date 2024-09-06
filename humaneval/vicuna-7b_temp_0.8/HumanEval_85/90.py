
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    half_odd_lst = lst[:]
    half_even_lst = []
    for i in range(len(half_odd_lst)):
        if half_odd_lst[i] % 2 == 0:
            half_even_lst.append(half_odd_lst[i])
            half_odd_lst.pop(i)
    return half_even_lst
