
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
    # We need to check if the number is less than 100 because we are not checking
    # the number of digits, but rather the number of digits when adding the elements.
    # We want to find the sum of elements with at most two digits. For example,
    # if we have an array of 5 elements with at least 3 digits, and k = 1, then
    # we can't add the elements from the first k elements because the sum will be
    # greater than 100.
    # We can use the following algorithm to find the sum of elements with at most
    # two digits:
    # 1. Initialize a sum variable to 0.
    # 2. Iterate over the first k elements of the array.
    # 3. For each element, add the element to the sum.
    # 4. If the sum is less than or equal to 100, add the element to the sum.
    # 5. Otherwise, return the sum.
    # Example:
    # Input: arr = [111,21,3,40
