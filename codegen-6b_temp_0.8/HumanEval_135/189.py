
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    def repeated_max_index(arr, index):
        max_value = arr[index + 1]
        candidate_index = index + 1
        for i in range(index + 2, len(arr)):
            if arr[i] not in arr[index+1:i]:
                max_value = arr[i]
                candidate_index = i
            if max_value < arr[i]:
                max_value = arr[i]
                candidate_index = i

        return candidate_index

    result = -1
    for i in range(len(arr)):
        if result < repeated_max_index(arr, i):
            result = repeated_max_index(arr, i)

    return result


assert can_arrange([1,2,4,3,5]) == 3
assert can_arrange([1,2,3]) == -1
assert can_arrange([11,13,14,23,24,25,32,9]) == 4
assert can_arrange([1,2,3,4,5]) == 4
assert can_arrange([1,3,2,4,5]) == 2


"""
SOlution Notes:
a. Use binary search to find the smallest value greater than arr[index].
b. Check that the value at index is not the smallest value greater than arr[index].
c. If a value is not found, return -1.

"""
