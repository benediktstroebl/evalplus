

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    l_copy = l.copy()
    # print("l: ", l)
    # print("l_copy: ", l_copy)

    # for i in range(len(l)):
    #     print("i: ", i)
    #     for j in range(i+1, len(l)):
    #         print("j: ", j)
    #         print("l_copy: ", l_copy)
    #         print("l_copy[i]: ", l_copy[i])
    #         print("l_copy[j]: ", l_copy[j])
    #         if l_copy[i] + l_copy[j] == 0:
    #             return True

    for i in range(len(l)):
        # print("i: ", i)
        for j in range(len(l)):
            # print("j: ", j)
            if i != j:
                # print("l_copy: ", l_copy)
                # print("l_copy[i]: ", l_copy[i])
                # print("l_copy[j]: ", l_copy[j])
                if l_copy[i] + l_copy[j] == 0:
                    return True

    return False



