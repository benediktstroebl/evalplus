

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
    # IMPLEMENT THIS FUNCTION

    pair_sum = []

    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i] + l[j] == 0:
                if l[i] > l[j]:
                    pair_sum.append(f"{l[j]} + {l[i]}")
                else:
                    pair_sum.append(f"{l[i]} + {l[j]}")
    if len(set(pair_sum)) == len(pair_sum):
        return False
    else:
        return True

    # if len(set(pair_sum)) == len(pair_sum):
    #     return False
    # else:
    #     return True

