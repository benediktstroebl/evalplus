
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    
    def index_of_max(arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j] <= arr[i]:
                    return j
        return None

    return index_of_max(arr)
