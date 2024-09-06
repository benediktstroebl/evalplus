

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # max = l[0]
    # for i in range(len(l)):
    #     if l[i] > max:
    #         max = l[i]
    # return max

    # num_list = [l[0]]
    # for i in range(1, len(l)):
    #     if l[i] > num_list[0]:
    #         num_list[0] = l[i]
    #     elif l[i] > num_list[1]:
    #         num_list[1] = l[i]
    # return num_list[0]

    if len(l) == 1:
        return l[0]
    if len(l) == 2:
        return max(l[0], l[1])
    else:
        return max(max_element(l[:2]) + max_element(l[2:]), l[0] + l[-1])

