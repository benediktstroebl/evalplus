
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
    assert k <= len(arr), f'k ({k}) should be smaller than len(arr) ({len(arr)})'

    # at most two digits -> we can use a queue
    # first k elements -> we can use a stack

    # we will add two elements to the queue
    # if the queue has more than 2 elements, remove the first element
    # if the stack has more than 2 elements, remove the last element

    queue = []
    stack = []

    for i, num in enumerate(arr):
        if len(queue) < 2:
            queue.append(num)
        elif len(stack) < 2:
            stack.append(num)
        else:
            break

        if i == k - 1:
            break

    result = 0
    if len(stack) >= 2:
        stack.pop()
        stack.pop()
        for num in stack:
            result += num
    if len(queue) >= 2:
        queue.pop(0)
        queue.pop(0)
        for num in queue:
            result += num

    return result
