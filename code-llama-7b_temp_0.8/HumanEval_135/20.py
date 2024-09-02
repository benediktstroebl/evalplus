
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # 1. Take the array arr
    # 2. Iterate over each element in the array
    # 3. If there is no element that is less than or equal to the current element
    # then return -1
    # 4. Return the index of the last element in the array

    for i in range(len(arr)):
        for j in range(i):
            if arr[j] <= arr[i]:
                return j
    return -1
