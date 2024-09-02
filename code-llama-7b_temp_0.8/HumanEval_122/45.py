
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
    print("arr input is: " + str(arr))
    arr_sum = 0
    num_digits_count = 0
    for index, num in enumerate(arr):
        print("Current num: " + str(num) + " at index: " + str(index))
        if index >= k:
            break
        if num > 9:
            num_digits_count += 1
        arr_sum += num

    return arr_sum - (10 ** num_digits_count - 1)
