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
    # Check if the list is empty
    if not x:
        return []

    # Use a dictionary to count the occurrence of each digit from 0 to 9 and exclude digits that are even
    even_digits = [digit for digit in range(10) if digit % 2 == 0]
    filtered_digits = {digit: x for digit, x in enumerate(x, 10) if digit not in even_digits}

    # Use a list to store the integers that have only odd digits
    result = [int(''.join(map(str, sorted(filtered_digits[digit])))) for digit in filtered_digits if filtered_digits[digit]]

    # Sort the result in increasing order
    result.sort()
    return result