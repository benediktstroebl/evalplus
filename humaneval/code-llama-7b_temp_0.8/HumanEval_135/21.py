
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) < 2:
        return -1
    else:
        result = [arr[0]]
        for i in range(1, len(arr)):
            if arr[i] > result[-1]:
                result.append(arr[i])
            else:
                left = 0
                right = len(result) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    if arr[i] < result[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                result.insert(left, arr[i])
        return len(result) - 1
