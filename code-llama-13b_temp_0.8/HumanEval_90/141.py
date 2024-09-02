
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
    nums = lst
    n = len(nums)
    if n < 2:
        return None

    if n == 2:
        return None

    min1 = float('inf')
    min2 = float('inf')
    for i in range(n):
        if nums[i] < min1:
            min2 = min1
            min1 = nums[i]
        elif nums[i] < min2:
            min2 = nums[i]
    return min2

