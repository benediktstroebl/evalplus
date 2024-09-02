
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
    #TODO: 7pts

    smallest_nums = sorted(lst)

    if len(smallest_nums) > 0:
        if smallest_nums[0] != smallest_nums[1]:
            return smallest_nums[1]
        else:
            return smallest_nums[2]

    else:
        return None

