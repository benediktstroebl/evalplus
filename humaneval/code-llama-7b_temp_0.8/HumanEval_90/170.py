
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

    def get_smallest(lst):
        # sort lst
        lst.sort()
        return lst[0]

    def get_next_smallest(lst):
        # check if list is empty
        if not lst:
            return None
        # create a list of all items after smallest
        lst_new = lst[lst.index(smallest) + 1 :]
        # check if list_new is empty
        if not lst_new:
            return None
        return get_smallest(lst_new)

    # get the smallest element
    smallest = get_smallest(lst)
    return get_next_smallest(lst)

