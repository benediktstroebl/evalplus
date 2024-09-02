
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
    arr.insert(0, -1)
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            stack.append(i)
        else:
            while stack and arr[i] < arr[stack[-1]]:
                prev = stack.pop()
                if stack:
                    print arr[stack[-1]], arr[i]
                    print prev, i
                else:
                    print arr[prev], arr[i]
            stack.append(i)
    print stack
    if stack:
        return stack[-1]
    else:
        return -1

