
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """

    # error cases
    if not isinstance(lst, list):
        raise TypeError('Please input a list!')
    if len(lst) == 0:
        raise ValueError('Cannot input an empty list!')
    if len(lst) % 2 == 0:
        raise ValueError('Cannot input an even-length list!')
    
    sum = 0
    for i in range(1, len(lst), 2):
        sum += lst[i]
    return sum
