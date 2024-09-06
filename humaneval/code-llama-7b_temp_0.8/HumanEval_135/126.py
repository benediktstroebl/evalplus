
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Find the max value in the array
    # Declare a second array, call it answer, and set all of it's values to -1
    # Then iterate through the array to find the max value
    # Once you find the max value, you want to compare the element at the max
    # value to the previous element
    # If the previous element is smaller than the max element, then you have
    # found an index that meets the criteria, and you should save that index
    # as the max value. Then you want to iterate through the array again, but
    # starting at the index of the previous max value and work your way
    # back to the end of the array.
    # If you find an index where the element at the index is greater than the
    # previous element, then you will return -1
    # If you do not find an index where the element at the index is greater
    # than the previous element, then you will return the index of the max
    # element

    # O(n) time | O(n) space - where n is the length of the array
    # in the worst case

    if len(arr) == 0:
        return -1
    else:
        max_value = arr[-1]
        for element in arr:
            if element >= max_value:
                max_value = element
            else:
                break

        if max_value <= arr[-1]:
            return -1

        answer = [-1] * (len(arr))
        answer[-1] = max_value
        max_index = len(arr) - 1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] >= answer[max_index - 1]:
                answer[max_index - 1] = arr[i]
                max_index -= 1
            else:
                return -1

        return max_index

    # if len(arr) == 0:
    #     return -1
    # else:
    #     max_value = arr[-1]
    #     for element in arr:
    #         if element >= max_value:
    #             max_value = element
