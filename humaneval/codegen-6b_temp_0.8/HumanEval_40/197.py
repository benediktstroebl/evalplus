

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
    assert l, 'list cannot be empty'

    l = [abs(v) for v in l]
    known_values = set()
    for i in l:
        if i in known_values:
            return True
        else:
            known_values.add(l[l.index(i)]-i)
    return False

assert triples_sum_to_zero([1, 3, 5, 0]) == False, 'Wrong result for [1, 3, 5, 0]'
assert triples_sum_to_zero([1, 3, -2, 1]) == True, 'Wrong result for [-2, 1, 3, -1]'
assert triples_sum_to_zero([1, 2, 3, 7]) == False, 'Wrong result for [1, 2, 3, 7]'
assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True, 'Wrong result for [2, -5, 3, 9, 7]'
assert triples_sum_to_zero([1]) == False, 'Wrong result for [1]'
