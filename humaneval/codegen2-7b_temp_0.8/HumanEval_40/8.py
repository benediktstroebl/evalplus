

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
    for i in range(len(l)):
        if l[i] < 0:
            continue
        elif l[i] == 0:
            return True
        elif i > 0 and l[i-1] < 0:
            continue
        else:
            j = i + 1
            k = len(l) - 1
            while j < k:
                sum_ = l[i] + l[j] + l[k]
                if sum_ == 0:
                    return True
                elif sum_ < 0:
                    j += 1
                else:
                    k -= 1
    return
