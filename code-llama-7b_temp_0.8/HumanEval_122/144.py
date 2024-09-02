
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

    def two_digit_sum(arr):
        """Sum the first two elements of a list of numbers."""
        return arr[0] + arr[1]

    # Note: if you are using a loop to iterate through a list, you can use
    # range() or enumerate() to create an index variable.
    # Example:
    # for index, value in enumerate(arr):
    #     print(f"{index}: {value}")

    # Note: if you want to use the last two digits of a number, use
    # last_two_digits = number % 100

    # Note: if you want to use the last digit of a number, use
    # last_digit = number % 10

    # Note: if you want to use the first digit of a number, use
    # first_digit = number // 10

    # Note: if you want to use the second digit of a number, use
    # second_digit = (number % 100) // 10

    total = 0

    for index in range(k):
        if arr[index] >= 10 and arr[index] <= 99:
            total += two_digit_sum(arr[index])
        else:
            total += arr[index]

    return total
