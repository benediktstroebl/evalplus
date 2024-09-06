
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    lst = [2, 6, 7]
    lst_even = []
    lst_odd = []

    for i in range(len(lst)):
        if i % 2 == 0:
            lst_even.append(lst[i])
        elif i % 2 == 1:
            lst_odd.append(lst[i])

    res = 0
    for i in range(len(lst_even)):
        res += lst_even[i]

    return res

