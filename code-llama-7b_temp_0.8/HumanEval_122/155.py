
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
    # max two digits -> array size < 100, use a map to map the sum of digits to sum
    two_digits_sum_map = {}
    two_digits_count = 0
    for i in range(len(arr)):
        if i >= k:
            break
        arr[i] = str(arr[i])
        if len(arr[i]) == 2:
            two_digits_sum_map[arr[i]] = 0
            two_digits_count += 1
        arr[i] = int(arr[i])
    
    for i in range(k):
        if i in two_digits_sum_map:
            two_digits_sum_map[i] += arr[i]

    if two_digits_count == 0:
        return sum(arr[:k])
    
    return sum(two_digits_sum_map.values())
