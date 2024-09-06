
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # 1)
    """
    lst_odd = []
    for i in lst:
        if i % 2 == 0:
            lst_odd.append(i)
    return sum(lst_odd)
    """
    # 2)
    """
    return sum([i for i in lst if i % 2 == 0])
    """
    # 3)
    """
    return sum(lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 == 0)
    """
    # 4)
    """
    even = [i for i in lst if i % 2 == 0]
    return sum(even[i] for i in range(1, len(even), 2))
    """
    # 5)
    """
    return sum(i for i in lst if i % 2 == 0)
    """
    # 6)
    """
    return sum(i for i in lst if i % 2 == 0 if i
