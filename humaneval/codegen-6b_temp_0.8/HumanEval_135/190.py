
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    arr_len = len(arr)

    def find_greater_than_and_not_equal_to_previous(index):
        if index == 0:
            return -1
        previous_value = arr[index-1]
        greater_than_previous = index - 1 - arr[:index-1].count(previous_value)
        if greater_than_previous >= arr[index-1]:
            return greater_than_previous
        else:
            return -1

    return max(range(arr_len), key=lambda index: find_greater_than_and_not_equal_to_previous(index))

