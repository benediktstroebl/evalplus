
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
    # TODO: write your solution here
    # next smallest number in the list.
    next_smallest_num = None
    if len(lst) >= 2:
        # First, remove duplicates.
        lst.sort()
        lst = list(set(lst))
        # Then, get the next smallest number.
        for i in range(1, len(lst)):
            if lst[i] != lst[i - 1] + 1:
                next_smallest_num = lst[i]
                break
    return next_smallest_num
