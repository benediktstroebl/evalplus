

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
    #convert to a set, then to a list (so we can rearrange it
    l = set(l)
    l = list(l)
    #sorted list lets us do this
    l = sorted(l)
    #shift the list to the right so we can access the negative elements
    l = l[::-1]
    #negative_list = [i for i in l if i < 0]
    pairs_sum_to_zero = False
    if len(l) == 0:
        return False
    elif len(l) == 1:
        return True
    elif l[0] == 0:
        if l[1] == 0:
            return False
        elif l[1] < 0:
            return True
    
    for i in range(len(l)-1):
        if l[i] < 0:
            #negative_list.append(l[i])
            #can also do this
            if l[-1] == l[i+1] - l[i]:
                pairs_sum_to_zero = True
            else:
                return False
    return pairs_sum_to_zero
    # else:
    #     return False
