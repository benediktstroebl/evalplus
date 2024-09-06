

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
    # 1. Create an empty dictionary
    # 2. Loop through the list
    # 3. For each item, check if the dictionary contains its "complement":
    #    if it does, return True, if not, add it to the dictionary.
    #    When the loop finishes, return False

    # dictionary = {}
    # for item in l:
    #     complement = 0 - item
    #     if complement in dictionary:
    #         return True
    #     else:
    #         dictionary[item] = item
    # return False

    # 1. Create an empty set
    # 2. Loop through the list
    # 3. For each item, check if the set contains its "complement":
    #    if it does, return True, if not, add it to the set.
    #    When the loop finishes, return False
    set1 = set()
    for item in l:
        complement = 0 - item
        if complement in set1:
            return True
        else:
            set1.add(item)
    return False

