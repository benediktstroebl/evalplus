
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
    digits = [int(d) for d in str(x)]
    while len(digits) > 1:
        for i in range(1, len(digits)):
            for j in range(i+1, len(digits)):
                if (digits[i] * 10 + digits[j]) % 10 != digits[j]:
                    digits.remove(digits[i])
                    digits.remove(digits[j])
                    break
    return digits
