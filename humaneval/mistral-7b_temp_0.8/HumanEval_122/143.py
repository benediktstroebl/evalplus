
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

    """
    My solution:

    It is important to understand that we are looking for summation of the
    elements with at most two digits.
    And the digits here refer to the digits in the string representation of
    the number.
    The algorithm is simple, we iterate through the input array arr
    and check the first two digits of the number.
    If the first two digits are less than or equal to 10, then we add
    that number to the total sum.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    total_sum = 0

    for i in arr:
        if str(i)[0:2] <= "99":
            total_sum += i

    return total_sum
