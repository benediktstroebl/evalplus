
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
    #find first smallest num
    smallest_num = min(lst)
    #find the first num after smallest that's smaller
    for num in lst:
        if num < smallest_num and num != smallest_num:
            return num
    return None

    #need to find the next smallest num after the smallest num, if it doesn't exist, it returns None
    #nums = [1, 2, 3, 4, 5]
    #nums = [5, 1, 4, 3, 2]
    #nums = []
    #nums = [1, 1]

