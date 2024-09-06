
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
    # assert type(x) == list, "x is not a list"
    # assert len(x) > 0, "x is empty"
    # assert all(type(i) == int for i in x), "Not all elements are integers"
    # assert all(i >= 0 for i in x), "Not all elements are positive"
    # assert all(str(j) for j in x), "Has element(s) with non-integer digits"
    # assert all(all(j % 2 != 0 for j in str(i)) for i in x), "Has even digit(s)"

    def has_even_digit(i):
        return any(i % 2 == 0 for i in str(i))
    return [i for i in x if not has_even_digit(i)]
