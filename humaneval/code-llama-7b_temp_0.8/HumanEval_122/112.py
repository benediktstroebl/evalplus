
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
    total_sum = sum(arr[:k])
    two_digit_sum = 0

    for n in arr[:k]:
        if n >= 10 and n <= 99:
            two_digit_sum += n
    
    return total_sum - two_digit_sum
