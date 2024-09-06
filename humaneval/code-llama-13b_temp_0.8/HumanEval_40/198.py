

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
    # Hint:  This method should return True or False
    # Hint:  Use set() to make a set from the list.  See if the set's
    #        length is less than 3.  If so, return False.
    # Hint:  You can find an element that sums to 0 with any two elements.
    # Hint:  You can find the sum of all elements in the list with a loop
    # Hint:  Don't forget to use the absolute value of a number
    # YOUR CODE HERE
    l = sorted(l)
    s = set(l)
    if len(s) < 3:
        return False
    else:
        for i in range(len(l) - 2):
            j = i + 1
            k = len(l) - 1
            while j < k:
                if abs(l[i]) + abs(l[j]) + abs(l[k]) == 0:
                    return True
                elif abs(l[i]) + abs(l[j]) + abs(l[k]) > 0:
                    k = k - 1
                else:
                    j = j + 1
        return False

