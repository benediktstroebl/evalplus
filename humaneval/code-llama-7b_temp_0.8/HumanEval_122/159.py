
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
    # TODO: Write your code here
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    from collections import deque
    queue = deque()
    queue.append(0)
    result = 0
    for x in arr:
        x = x % 100
        if len(queue) < k:
            queue.append(x)
        else:
            result += (queue.popleft() + x) % 100
            queue.append(x)
    return result

