
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Final index is -1 if there are no more elements to check
    def helper(i):
        if i == len(arr):
            return -1
        elif arr[i] >= arr[i-1]:
            return helper(i+1)
        else:
            return arr[i-1]
    # Run these helper functions until they don't return -1
    for i in range(1, len(arr)):
        if helper(i) == -1:
            return -1
    # If all helper functions returned -1 then the array can be arranged
    return True
