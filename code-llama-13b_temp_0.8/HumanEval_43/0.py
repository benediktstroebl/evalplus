

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
    # 1. This is a possible solution using a dictionary
    # d = {}
    # for i in l:
    #     if -i in d:
    #         return True
    #     d[i] = 1
    # return False

    # 2. This is a possible solution using nested loops
    # for i in range(len(l)):
    #     for j in range(i+1, len(l)):
    #         if l[i] + l[j] == 0:
    #             return True
    # return False

    # 3. This is a possible solution using a set
    # seen = set()
    # for i in l:
    #     if 0 - i in seen:
    #         return True
    #     seen.add(i)
    # return False

    # 4. This is a possible solution using a list
    seen = []
    for i in l:
        if 0 - i in seen:
            return True
        seen.append(i)
    return False
