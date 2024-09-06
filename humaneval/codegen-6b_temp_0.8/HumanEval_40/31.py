

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
    # your code here
    sum_array = []
    for num in l:
        if (num != 0 and num not in sum_array):
            sum_array.append(num)
            for num_2 in l:
                if (num_2 != 0 and num_2 != num and num_2 not in sum_array):
                    if (num + num_2 == 0):
                        return True
    return False
    
 