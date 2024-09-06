

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
    #Hint: Try creating a dictionary
    # dict = {}
    # for item in l:
    #     if item in dict:
    #         dict[item] += 1
    #     else:
    #         dict[item] = 1
    # for key in dict:
    #     if (-1 * key) in dict:
    #         return True
    # return False

    #Hint: Try sorting the list and going through it once
    # l.sort()
    # for i in range(len(l)-1):
    #     if l[i] + l[i+1] == 0:
    #         return True
    # return False

    #Hint: Think about the problem in terms of set intersection
    #still not sure how to use this
    # s1 = set(l)
    # s2 = set([0-x for x in l])
    # return bool(s1.intersection(s2))

    # Hint: Think about the problem in terms of the complement of each element
    seen = {}
    for num in l:
        if 0 - num in seen:
            return True
        seen[num] = True
    return False

