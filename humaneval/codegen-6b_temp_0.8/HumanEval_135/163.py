
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr.sort()

    def greedy_finder(index):
        if index >= len(arr)-1:
            return -1

        for i in range(index+1, len(arr)):
            if arr[index] < arr[i]:
                return i
        return -1

    return greedy_finder

