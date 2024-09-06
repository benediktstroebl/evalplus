
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
    def digit_sum(n):
        return sum(int(d) for d in str(n))

    for i in range(k):
        max_val = 0
        for num in arr:
            if digit_sum(num) > max_val:
                max_val = digit_sum(num)
        if max_val > 9:
            return 0
        arr = [num for num in arr if digit_sum(num) <= max_val]
    return sum(arr)

