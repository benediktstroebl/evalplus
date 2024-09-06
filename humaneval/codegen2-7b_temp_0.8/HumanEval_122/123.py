
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
    i = k
    sum_of_two = 0
    while i < len(arr):
        num = arr[i]
        i += 1
        if num >= 1000:
            if num >= 10000:
                sum_of_two += num
                i += 1
            else:
                sum_of_two += (num // 100) + (num % 100)
        else:
            sum_of_two += num
    return sum_of_two

