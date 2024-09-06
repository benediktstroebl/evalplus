

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # max_list = []
    # for x in l:
    #     if len(max_list) == 0:
    #         max_list.append(x)
    #     elif x > max_list[0]:
    #         max_list[0] = x

    # return max_list[0]
    return reduce(lambda x, y: max(x, y), l)
