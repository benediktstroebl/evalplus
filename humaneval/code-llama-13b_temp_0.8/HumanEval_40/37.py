

def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    # start with the brute force version
    # for each pair of elements in the list,
    # check if the sum of the pair equals the third element in the list
    # return True if you find one, otherwise return False

    # start with the brute force version
    # for each pair of elements in the list,
    # check if the sum of the pair equals the third element in the list
    # return True if you find one, otherwise return False

    # for i in range(len(l)):
    #     for j in range(i + 1, len(l)):
    #         for k in range(j + 1, len(l)):
    #             if l[i] + l[j] + l[k] == 0:
    #                 return True
    # return False
    # avoid using i, j, k as variable names because they're also common function names
    # to avoid confusion, use a, b, c
    for a in range(len(l)):
        for b in range(a + 1, len(l)):
            for c in range(b + 1, len(l)):
                if l[a] + l[b] + l[c] == 0:
                    return True
    return False

