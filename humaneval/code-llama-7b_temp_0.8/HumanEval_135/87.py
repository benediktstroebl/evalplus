
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if not arr or len(arr) < 2:
        return -1
    else:
        # since the array will not contain duplicate values, we can count the
        # elements as we go
        # we know that the first index must be >=0
        index_of_last_smaller_element = 0
        for i in range(1, len(arr)):
            # if the current element is larger than the last one, then the
            # last one must be the index of the largest smaller element
            # or the last smaller element
            if arr[i] >= arr[i-1]:
                index_of_last_smaller_element = i - 1
            # if the current element is smaller than the last one, then the
            # last one cannot be a smaller element
            else:
                index_of_last_smaller_element = max(
                    index_of_last_smaller_element, i - 1
                )
        # the last element in the array can't be smaller than the last smaller
        # element
        if arr[-1] >= arr[index_of_last_smaller_element]:
            return -1
        else:
            return index_of_last_smaller_element

