

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
    # creating a set for efficiency
    s = set(l)

    # The code below is the answer
    return any(map(lambda x: x * -1 in s, s))


    # Code below is my answer.  I'm not sure if it is as efficient
    """
    counter = {}
    for x in l:
        if x not in counter:
            counter[x] = 0
        counter[x] += 1
    for x in l:
        if -x in counter and x != -x:
            return True
    return False
    """


    # Code below is me, but I'm still trying to improve the efficiency
    """
    s = set(l)
    counter = {}
    for x in s:
        if x not in counter:
            counter[x] = 0
        counter[x] += 1
    for x in s:
        if -x in s and x != -x:
            return True
    return False
    """
