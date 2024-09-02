
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
    for i in arr:
        if not stack or i > stack[-1]:
            stack.append(i)
        else:
            while stack and i <= stack[-1]:
                stack.pop()
            if not stack or i > stack[-1]:
                stack.append(i)
    return -1 if stack else stack[-1]

