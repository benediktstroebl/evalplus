
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    if len(arr) <= 1:
        return -1
    stack = []
    for i, v in enumerate(arr):
        while stack and arr[stack[-1]] < v:
            stack.pop()
        if not stack or arr[stack[-1]] != v:
            stack.append(i)
    return stack[0] if len(stack) > 1 else -1

