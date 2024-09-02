
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    nums = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and lst[i] % 2 == 0:
            nums += lst[i]
    return nums
