
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    if len(arr) < 2:
        return 0

    stack = []
    for i in range(len(arr)):
        stack.append(arr[i])

    if stack == stack[::-1]:
        return 0

    num_changes = 0
    while len(stack) > 0:
        top_num = stack.pop()
        print(stack)
        if stack == stack[::-1]:
            return num_changes
        print(stack)
        for i in range(len(stack)):
            if stack[i] != top_num:
                stack.insert(i, top_num)
                break
        num_changes += 1

    return num_changes

