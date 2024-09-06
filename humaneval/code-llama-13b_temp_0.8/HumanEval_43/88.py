

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
    # YOUR CODE HERE

    # raise NotImplementedError
    #a=[2, 4, -5, 3, 5, 7]
    #b=len(a)
    #c=0
    #for i in range(b):
        #for j in range(b):
            #if a[i]==a[j]:
                #continue
            #else:
                #if a[i]+a[j]==0:
                    #return True
        #return False



    b=len(l)
    c=0
    for i in range(b):
        for j in range(b):
            if l[i]==l[j]:
                continue
            else:
                if l[i]+l[j]==0:
                    return True
    return False


