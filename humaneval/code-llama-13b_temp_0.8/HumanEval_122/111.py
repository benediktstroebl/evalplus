
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
    two_digit_numbers = 0
    one_digit_numbers = 0
    total = 0

    for number in arr:
        if number > 99:
            two_digit_numbers += 1
        if 0 <= number <= 9:
            one_digit_numbers += 1
        if two_digit_numbers + one_digit_numbers == k:
            break

    print(two_digit_numbers, one_digit_numbers)
    for i in range(k):
        total += arr[i]
    return total

