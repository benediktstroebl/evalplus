
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
    unique = []
    even_digits = ['2', '4', '6', '8']
    for num in x:
        num = str(num)
        if num[0] == '0':
            continue
        has_even = False
        for digit in num:
            if digit in even_digits:
                has_even = True
                break
        if not has_even:
            unique.append(num)
    return sorted(unique)

