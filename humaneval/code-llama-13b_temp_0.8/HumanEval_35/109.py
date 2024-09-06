

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # def max_element_helper(l, i, curr_max):
    #     if i == len(l):
    #         return curr_max
    #     if l[i] > curr_max:
    #         curr_max = l[i]
    #     return max_element_helper(l, i + 1, curr_max)
    # return max_element_helper(l, 0, -float('inf'))

    # iterative
    curr_max = -float('inf')
    for i in l:
        if i > curr_max:
            curr_max = i
    return curr_max

