

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
    # triples_sum_to_zero: None -> bool
    "*** YOUR CODE HERE ***"
    if len(l) == 0:
        return False
    elif len(l) == 1:
        return None
    else:
        dict = {}
        for i in l:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        for i in dict.items():
            if -i[1] in dict and i[1] in dict and i[1] != 0 and i[1] != -i[1]:
                return True
    return False

