

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
    """
    All the elements have to be distinct
    So if we encounter a duplicate element we can break
    """
    uniques = []
    for i in l:
        if i not in uniques:
            uniques.append(i)
        else:
            return False
    print(uniques)
    for i in range(len(uniques)):
        for j in range(i + 1, len(uniques)):
            if uniques[i] + uniques[j] == 0:
                return True
    return False
