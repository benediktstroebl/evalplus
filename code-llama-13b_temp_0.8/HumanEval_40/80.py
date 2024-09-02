

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
    # One way to do it:
    # l1 = list(set(l))
    # for i in range(len(l1)):
    #     for j in range(i + 1, len(l1)):
    #         if - l1[i] - l1[j] in l1[j + 1:]:
    #             return True
    # return False

    # Faster way:
    l1 = list(set(l))
    if len(l1) < 3:
        return False
    l1.sort()
    for i in range(len(l1) - 2):
        j = i + 1
        k = len(l1) - 1
        while j < k:
            if l1[i] + l1[j] + l1[k] == 0:
                return True
            elif l1[i] + l1[j] + l1[k] < 0:
                j += 1
            else:
                k -= 1
    return False

