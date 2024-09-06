

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
    # Your code here
    hash_map = {}
    for i in range(len(l)):
        if l[i] not in hash_map:
            hash_map[l[i]] = 1
        else:
            hash_map[l[i]] += 1
    for i in range(len(l)):
        if l[i] * -1 in hash_map and l[i] * -1!= l[i]:
            return True
    return False
