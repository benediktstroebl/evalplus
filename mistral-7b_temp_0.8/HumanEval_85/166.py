
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    sum_of_even = 0
    for i in range(len(lst) - 1):
        if (i + 1) % 2 == 0 and lst[i] % 2 == 0:
            sum_of_even = sum_of_even + lst[i]
    return sum_of_even
