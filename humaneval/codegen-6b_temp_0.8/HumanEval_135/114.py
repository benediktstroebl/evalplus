
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    stack = []
    for i in range(len(arr)):
        if not stack:
            stack.append(i)
        elif arr[i] > arr[stack[-1]]:
            stack.append(i)
        else:
            while stack[-1] > i and arr[i] < arr[stack[-1]]:
                stack.pop()
            if not stack:
                stack.append(i)
            else:
                stack.append(i)

    if stack:
        return stack.pop()
    return -1

