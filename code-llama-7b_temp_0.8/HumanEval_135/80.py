
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # What is the highest element in the array?
    # For each element in the array:
    #   If the element is greater than the highest element seen so far, what is
    #   the largest index of a smaller element?
    #   Keep track of the largest index for each element.
    # If there is an element that is not greater than or equal to the preceding
    # element, return the maximum index. If there is no element, return -1.
    # O(n) time, O(n) space
    # Can we do better?
    # Can we do better with only one pass?
    # Can we do better with a more complex data structure?

    highest_element = max(arr)
    largest_index_for_element = {e: -1 for e in arr}

    for i, e in enumerate(arr):
        if largest_index_for_element[e] == -1:
            continue
        largest_index_for_element[e] = i

    for i, e in enumerate(arr):
        if arr[i] > e:
            largest_index_for_element[e] = max(largest_index_for_element[e], i)

    for e in arr:
        if largest_index_for_element[e] == -1:
            return -1

    return max(largest_index_for_element.values())

