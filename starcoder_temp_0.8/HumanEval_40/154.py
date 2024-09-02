

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
    # begin solution
    n = len(l)
    if n < 3:
        return False
    l = sorted(l)
    #for i in range(n):
        #if l[i] == 0:
            #return True
    #for i in range(n-2):
        #if l[i] == 0:
            #for j in range(i+1, n-1):
                #if l[j] == -l[i] and l[j+1] == -l[i]:
                    #return True
    #return False
    for i in range(n-2):
        if l[i] == 0:
            for j in range(i+1, n-1):
                if l[j] == -l[i] and l[j+1] == -l[i]:
                    return True
    return False
    # end solution
