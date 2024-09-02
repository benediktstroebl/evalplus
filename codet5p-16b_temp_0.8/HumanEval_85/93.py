
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    even = [num for num in lst if num % 2 == 0]
    res = 0
    for i in range(len(even)):
        if i % 2 == 1:
            res += even[i]
    return res
