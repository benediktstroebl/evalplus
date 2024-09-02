
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

    # Used to store the sum of the first k elements
    # 2 digits or less, of the original array,
    # but only if k elements are present.
    sum_of_2_digits_or_less = 0

    # Traverse the array using a for loop
    for i in range(k):

        # Check the number of digits of the current element, i
        num_digits = len(str(arr[i]))

        # If the current element has 2 or less digits
        # then add it to the total sum.
        if num_digits <= 2:
            sum_of_2_digits_or_less += arr[i]

    return sum_of_2_digits_or_less

