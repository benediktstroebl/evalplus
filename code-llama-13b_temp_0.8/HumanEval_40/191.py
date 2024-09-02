

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
    #start with an empty set, set_i
    set_i = set()
    #make a for loop to loop through each element of list l
    for i in l:
        #if the current element is not in set_i then add it to set_i
        if i not in set_i:
            set_i.add(i)
        #else
        else:
            #make a for loop to loop through each element of list l
            for j in l:
                #if the current element is not in set_i then add it to set_i
                if j not in set_i:
                    set_i.add(j)
                #else
                else:
                    #make a for loop to loop through each element of list l
                    for k in l:
                        #if the current element is not in set_i then add it to set_i
                        if k not in set_i:
                            set_i.add(k)
                        #else
                        else:
                            #if i + j + k equals zero return True
                            if i + j + k == 0:
                                return True
                            #else return False
                            else:
                                return False
