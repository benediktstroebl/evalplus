
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def count(i):
        count = 0
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                count += 1
        return count

    max_index = -1
    for i in range(1, len(arr)):
        max_index = max(max_index, count(i))
    return max_index
