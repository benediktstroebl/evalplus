
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
    # sort the list
    sorted_list = sorted(x)
    # for each element in the list
    for num in sorted_list:
        # for each digit in the number
        digit = str(num)
        # if all digits are odd
        if all(digit[i] % 2 != 0 for i in range(len(digit))):
            # print the number
            print(num)
            # return the number
            return [num]
    # return an empty list if no elements are found
    return []
