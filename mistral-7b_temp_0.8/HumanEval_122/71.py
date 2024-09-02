
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
    # Write your code here.
    sum_of_first_k = sum(arr[:k])
    sum_of_at_most_two_digit_elements = 0
    for element in arr[:k]:
        if len(str(element)) <= 2:
            sum_of_at_most_two_digit_elements += element
    return sum_of_at_most_two_digit_elements + sum_of_first_k - sum_of_at_most_two_digit_elements
