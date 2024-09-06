

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
    my_dict = {}

    for i in range(len(l)):
        if l[i] in my_dict:
            my_dict[l[i]] += 1
        else:
            my_dict[l[i]] = 1

    for j in range(len(l)):
        if l[j] in my_dict:
            if l[j] - l[j] in my_dict:
                return True
            elif l[j] + l[j] in my_dict:
                return True
            else:
                continue
        else:
            continue

