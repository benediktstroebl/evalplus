

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # def helper(l, max, index):
    #     if index == len(l):
    #         return max
    #     if l[index] > max:
    #         max = l[index]
    #     return helper(l, max, index + 1)
    # return helper(l, l[0], 0)
    max = l[0]
    for element in l:
        if element > max:
            max = element
    return max

