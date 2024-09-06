
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    # if len(lst) <= 1:
    #     return None
    # else:
    #     lst.sort()
    #     return lst[1]
    n = len(lst)
    if n < 2:
        return None

    # we want to find the next smallest
    # element, so we have a max heap
    lst.sort()

    # to rebalance the heap, we need to
    # call n.children() - 1 times to get to
    # the root of the heap
    heapq._heapify_max(lst)
    for i in range(n-2):
        heapq._heapify_max(lst)
    
    return heapq._heapreplace_max(lst, lst[0])

