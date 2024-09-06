
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    list_even = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i % 2 != 0:
            list_even.append(lst[i])

    sum_even = sum(list_even)
    return sum_even
