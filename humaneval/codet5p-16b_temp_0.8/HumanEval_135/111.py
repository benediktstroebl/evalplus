
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    
    if len(arr) == 1:
        return -1

    stack = []

    for i in range(len(arr)):
        if not stack or stack[-1] <= arr[i]:
            stack.append(arr[i])
        else:
            while stack and stack[-1] > arr[i]:
                stack.pop()
            if not stack or stack[-1] <= arr[i]:
                stack.append(arr[i])
            else:
                return i-1

    return -1


