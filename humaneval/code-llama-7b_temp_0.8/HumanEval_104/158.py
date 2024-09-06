
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
    answer = []
    for i in x:
        s = str(i)
        all_digit = "".join(s)
        unique_digit = "".join(set(all_digit))
        for j in unique_digit:
            if int(j) % 2 == 0:
                answer.append(i)
    return sorted(answer)

