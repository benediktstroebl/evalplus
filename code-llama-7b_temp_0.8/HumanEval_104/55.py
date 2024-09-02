
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
    # Your code here
    new_list = list()
    for number in x:
        new_number = "".join([i for i in str(number) if int(i) % 2 != 0])
        if new_number != "":
            new_list.append(int(new_number))
    return sorted(new_list)

