

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
    # write your code here
    l.sort()

    # if there are only 2 elements in the list, return False
    if len(l) < 3:
        return False

    # iterate through the list, checking if any three elements sum to zero
    for i in range(len(l) - 2):
        j = i + 1
        k = len(l) - 1

        # if any three elements sum to zero, return True
        while j < k:
            sum = l[i] + l[j] + l[k]
            if sum == 0:
                return True
            elif sum > 0:
                k -= 1
            else:
                j += 1

    # if no three elements sum to zero, return False
    return False
