
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # O(n) time | O(1) space
    if len(arr) < 2:
        return -1
    # Track the max value in the array and the index of the last occurrence of
    # the max value.
    max_val = arr[0]
    max_val_index = 0
    # The index of the previous element
    prev_index = 0

    for i in range(1, len(arr)):
        if arr[i] > max_val:
            # If a greater element is encountered, update max_val and the index
            # of the last occurrence of the max value.
            max_val = arr[i]
            max_val_index = i
        elif arr[i] < arr[prev_index] and arr[i] < max_val:
            # If a lesser element is encountered that is smaller than the
            # current max_val, and is smaller than the previous element, then
            # there is a possibility of returning the index of this element.
            if arr[i] >= arr[prev_index]:
                return -1
            max_val = arr[i]
            max_val_index = i
        prev_index = i

    if max_val_index <= 0:
        return -1
    else:
        return max_val_index - 1
