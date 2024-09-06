
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # your code here
    list_of_unique_elements = []
    for item in x:
        unique_item = True
        for digit in str(item):
            if int(digit) % 2 == 0:
                unique_item = False
                break
        if unique_item:
            list_of_unique_elements.append(item)
    return sorted(list_of_unique_elements)
