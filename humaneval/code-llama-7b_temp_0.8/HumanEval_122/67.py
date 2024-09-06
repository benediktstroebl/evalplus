
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

    def two_digits(num):
        # Python strings are iterable
        for char in num:
            if char.isdigit():
                break
        else:
            return 0
        if char.isdigit():
            return 1
        return 0

    def sum_two_digits(num):
        sum = 0
        for digit in str(num):
            if digit.isdigit():
                sum += int(digit)
        return sum

    sum_two = sum_two_digits(arr[0])
    for num in arr[1:k]:
        sum_two += sum_two_digits(num)
    return sum_two

