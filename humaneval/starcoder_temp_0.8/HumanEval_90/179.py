
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

    # convert lst to a set to remove duplicates
    s = set(lst)

    # iterate over the set and find the 2nd smallest item
    # O(n) time
    # O(1) space
    for i in sorted(s):
        if i + 1 in s:
            return i + 1

    # no 2nd smallest item was found
    return None

