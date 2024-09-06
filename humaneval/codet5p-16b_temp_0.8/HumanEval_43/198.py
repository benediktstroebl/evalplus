

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """

    my_dict = {}
    for index in range(len(l)):
        try:
            my_dict[l[index]].append(index)
        except KeyError:
            my_dict[l[index]] = [index]

    for key in my_dict:
        if (key * -1) in my_dict:
            for value in my_dict[key]:
                for index in my_dict[key]:
                    if value!= index:
                        return True
    return False
