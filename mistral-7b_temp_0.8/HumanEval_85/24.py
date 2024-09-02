
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    if not lst:
        raise TypeError("Invalid list")

    # Write your code here
    result = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            result += lst[i]

    return result
