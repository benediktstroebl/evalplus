
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # Fill in your solution here

    def can_arrange_helper(arr, result):
        if len(arr) == 0:
            return result
        max_next = arr[0]
        for i in range(len(arr) - 1, -1, -1):
            if (arr[i] >= max_next):
                max_next = arr[i]
            else:
                result = i
                break

        if(result == -1):
            return -1
        else:
            return result + 1

    return can_arrange_helper(arr, -1)


assert can_arrange([1, 2, 4, 3, 5]) == 3
assert can_arrange([1, 2, 3]) == -1
assert can_arrange([1, 2, 3, 4]) == -1
assert can_arrange([1, 2, 4, 6]) == 0
assert can_arrange([]) == -1
assert can_arrange([1, 2, 3, 4, 5]) == -1
assert can_arrange([1, 2, 3, 4, 5, 6]) == -1
assert can_arrange([2, 1, 2, 3]) == 1
assert can_arrange([2, 3, 1]) == 1
assert can_arrange([3, 1, 2]) == 1
