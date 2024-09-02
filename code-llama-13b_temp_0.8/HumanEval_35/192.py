

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    # we will use max() function with key parameter
    # this parameter is a function which will be applied to
    # each element of a sequence (list) before comparision

    # abs() - returns absolute value
    # lambda x: ... - anonymous function which returns
    # ... which is just a function expression
    # this function expression is applied to each element of the list
    # and returns value on which max() will operate
    # so the algorithm finds the maximum of absolute values of elements of list

    return max(l, key=lambda x: abs(x))
