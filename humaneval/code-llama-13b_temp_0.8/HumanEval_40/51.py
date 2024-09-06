

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
    # +++your code here+++
    # LAB(begin solution)
    # 17min
    seen = {}
    for i in l:
        if i not in seen:
            seen[i] = 0
        seen[i] += 1
    for i in l:
        if -i in seen:
            if i == -i:
                if seen[i] >= 2:
                    return True
            else:
                return True
    return False
    # LAB(replace solution)
    # replace-triples_sum_to_zero




