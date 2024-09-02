
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    # first, we'll create a stack for the numbers that we've been looking at.
    # We'll push the first k numbers onto the stack.
    # Then, we'll loop over the rest of the numbers.
    # For each of these numbers, we'll check whether the top number of the stack
    # has two digits, and whether it's <= than the current number.
    # If so, we'll pop the number off the stack, add the current number to the total,
    # and push the current number back on the stack.

    # otherwise, we'll just push the current number onto the stack

    total = 0
    stack = []
    for i in range(k):
        stack.append(arr[i])

    for i in range(k, len(arr)):
        if len(stack) > 0 and stack[-1] <= arr[i] and len(str(stack[-1])) == 2:
            total += arr[i] - stack.pop()
            stack.append(arr[i])
        else:
            stack.append(arr[i])

    # now let's add together all of the numbers on the stack
    while len(stack) > 0:
        total += stack.pop()
    return total































