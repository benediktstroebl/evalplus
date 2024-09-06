
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
    result = []
    for num in x:
        all_digits_same = True
        digit_count = {}
        while num > 0:
            digit = num % 10
            if digit % 2 == 0:
                all_digits_same = False
                break
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1
            num //= 10
        if all_digits_same:
            result.append(num)

    return result

