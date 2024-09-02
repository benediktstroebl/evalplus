
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Check for duplicate values. If no duplicate values, return -1.
    cache = {}
    for i in range(len(arr)):
        if arr[i] in cache:
            return -1
        cache[arr[i]] = True
    
    # Brute force algorithm:
    #   O(n^2)
    # for i in range(len(arr) - 1):
    #     for j in range(i + 1, len(arr)):
    #         if arr[j] <= arr[i]:
    #             return j
    # return -1
    
    # Sort the list
    #   O(n log(n))
    arr = sorted(arr)
    
    # Iterate the sorted array
    #   O(n)
    last_el = arr[0]
    for i in range(1, len(arr)):
        el = arr[i]
        if el <= last_el:
            return i
        last_el = el
    return -1
