

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
    '''
    count = 0
    for x in range(len(l) - 1):
        for y in range(x + 1, len(l)):
            for z in range(y + 1, len(l)):
                if (l[x] + l[y] + l[z] == 0):
                    count += 1
    '''
    count = 0
    s = set()
    for i in l:
        if -i in s:
            count += 1
        s.add(i)
    return count >= 1
