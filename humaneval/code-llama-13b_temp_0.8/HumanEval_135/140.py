
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Check array has length at least 2.
    if len(arr) < 2:
        return -1
    
    # Create a dictionary to hold all the numbers.
    nums = {}
    
    # Populate the dictionary with the numbers and their counts.
    for i in arr:
        if i in nums:
            nums[i] += 1
        else:
            nums[i] = 1
    
    # Find the smallest number in the dictionary.
    min_num = min(nums.keys())
    
    # Iterate over the dictionary keys in reverse order.
    for k in sorted(nums.keys(), reverse = True):
        
        # If the key is the smallest number then check the value of the
        # smallest key - 1. If the key is greater then return the key as the
        # index of the first misplaced number.
        if k == min_num:
            if nums[min_num - 1] > 0:
                return -1
        
        # Check if the key is 1 larger than the smallest number. If it is then
        # return the key as the index of the first misplaced number.
        elif k == (min_num + 1):
            return k
    
    # Return -1 if no misplaced numbers found.
    return -1
    
