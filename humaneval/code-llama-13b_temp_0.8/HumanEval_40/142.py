

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
    # The only way to have three distinct elements which sum to zero is if
    # one of them is 0, and the other two sum to 0.
    if 0 in l:
        for element in l:
            # if we find another zero, we know the other two sum to 0
            if element == 0:
                return True
        return False
    else:
        # if we don't have a zero, we need to have three distinct elements.
        if len(l) < 3:
            return False
        else:
            # create a set so we can check for distinct elements.
            s = set()
            for element in l:
                if element in s:
                    # if an element is already in the set, we know we have a
                    # non-distinct element, so return False.
                    return False
                else:
                    # if the element isn't already in the set, add it.
                    s.add(element)
            # if we get here, we have three distinct elements.
            # now we need to find three elements that sum to 0.
            # we do this by checking to see if the sum of any two elements
            # are 0.
            for i in l:
                for j in l:
                    # if i + j == 0:
                    #     return True
                    # this is what we want, but let's make sure that i and j
                    # are not the same element.
                    if i != j and i + j == 0:
                        return True
                    # if we don't find a pair that sums to 0, we return False.
            return False

