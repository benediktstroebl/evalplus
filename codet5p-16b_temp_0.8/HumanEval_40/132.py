

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

    l.sort()
    for i in range(len(l) - 2):
        if i!= 0 and l[i] == l[i-1]:
            continue
        for j in range(i+1, len(l)-1):
            if j!= i+1 and l[j] == l[j-1]:
                continue
            k = l[i] + l[j]
            if k == 0:
                if j - i == 1:
                    return True
                elif j - i == 2:
                    return True
                else:
                    continue
            else:
                if k < 0:
                    break
                else:
                    continue

    return False

