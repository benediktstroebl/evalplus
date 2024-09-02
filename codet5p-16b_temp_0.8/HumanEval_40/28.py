

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

    zero_list = []
    for i in range(len(l)):
        if l[i] == 0:
            zero_list.append(i)
    if len(zero_list) < 3:
        return False
    else:
        for i in range(len(zero_list)-1):
            for j in range(i+1, len(zero_list)):
                if zero_list[i]!= zero_list[j]:
                    if zero_list[i] + zero_list[j] in l and zero_list[i] + zero_list[j] not in zero_list:
                        return True
    return False

