
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
    two_digit_sum = 0
    arr_len = len(arr)
    for index in range(k):
        if index < arr_len:
            arr_element = str(arr[index])
            if len(arr_element) == 2:
                two_digit_sum += arr[index]
            elif len(arr_element) == 3:
                two_digit_sum += int(arr_element[0]) + int(arr_element[1])
    return two_digit_sum

