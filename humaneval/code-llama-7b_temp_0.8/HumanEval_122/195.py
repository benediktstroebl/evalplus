
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
    # 1. Slow Solution
    # return sum([a for a in arr if len(str(a)) <= 2][:k])

    # 2. Optimized Solution
    # 2.1. Use a queue
    queue = []
    for i in range(min(k, len(arr))):
        queue.append(arr[i])

    # 2.2. Enqueue the next element if it is within the range of two digits
    for i in range(min(k, len(arr))):
        if len(str(queue[-1])) > 2:
            break

        if i < len(arr) - 1:
            queue.append(arr[i + 1])

    return sum(queue)

