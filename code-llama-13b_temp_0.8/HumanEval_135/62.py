
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Make a set of the negative numbers
    neg = set(i for i in arr if i < 0)
    
    # Make a dict of the indices of each number
    dict = {}
    for i in range(len(arr)):
        dict[arr[i]] = i
    
    # If all numbers are positive, return -1
    if len(neg) == 0:
        return -1
    
    # Traverse the array
    for i in range(len(arr)):
        # Check if current number is negative and there is an index of its
        # positive version
        if arr[i] < 0 and dict[abs(arr[i])] != i:
            return i
    return -1
        
