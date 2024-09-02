
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

    # Assume list only contains positive integers.
    # Convert list to string, then to list, to get list of individual digits.
    # Convert digits to integer, to ensure only digits are present.
    # Finally, sort the list of digits.
    # Digits in original list will only be unique if sorted list of digits is unique
    list_of_digits = [int(i) for i in str(x)]
    list_of_digits.sort()
    result = list(set(list_of_digits))
    return result

