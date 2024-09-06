

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    """sorting takes O(nlog(n))"""
    #start = time.time()
    t = [x for x in l if x%3!=0] #take the values from l that are not divisible by 3 and put them in t
    s = [x for x in l if x%3==0] #take the values from l that are divisible by 3 and put them in s
    s = list(sorted(s)) #sort the elements in s in ascending order
    t.extend(s) #put the elements in t in the end of t
    #elapsed_time = time.time()-start
    #print(elapsed_time)
    return t
