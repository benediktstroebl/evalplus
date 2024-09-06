
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # check condition
    if len(lst) == 0:
        return 0

    # get the number of odd elements and even elements
    odd_elements = 0
    even_elements = 0

    for i in lst:
        if i % 2 == 0:
            even_elements += i
        else:
            odd_elements += i

    # return the sum of the odd-indexed elements
    return odd_elements
