
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
    stack = []
    for i in range(len(arr)):
        if len(stack) == k:
            current_digit = arr[stack[-1]]
            sum_of_current_digit = sum(
                [arr[i] for i in stack if i < k and arr[i] <= current_digit * 10]
            )
            if sum_of_current_digit < current_digit:
                break
        stack.append(i)
    return sum(arr[stack[-1]] * i for i in range(
