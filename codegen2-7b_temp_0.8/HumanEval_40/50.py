

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
    
    if len(l) < 3:
        return False
    
    triples = [[]]
    for i in l:
        new_triples = []
        for triple in triples:
            for j in range(3):
                new_triple = triple[:]
                new_triple.append(i)
                new_triples.append(tuple(new_triple))
        triples = new_triples
    
    return len(set(triples)) < len(l)


