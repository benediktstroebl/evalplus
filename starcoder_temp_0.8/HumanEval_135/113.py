
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # using a stack we can achieve O(n) time with O(1) space
    stack = []
    for i, n in enumerate(arr):
        if len(stack) == 0 or stack[-1][0] <= n:
            stack.append((n, i))
        else:
            while len(stack) > 0 and stack[-1][0] > n:
                _, idx = stack.pop()
            if len(stack) == 0 or stack[-1][0] < n:
                return -1
            stack.append((n, idx))
    # if we've iterated through the whole array and the stack is empty
    # then the original array is in decreasing order
    if len(stack) == 0:
        return -1
    # stack[-1] is the largest element in the array
    return stack[-1][1]
