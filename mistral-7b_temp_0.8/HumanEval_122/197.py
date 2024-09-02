
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

    # 1. init output variable
    sum_of_k_digits = 0

    # 2. determine the total number of digits in the first k elements
    total_k_digits = len(str(k)) + sum(len(str(n)) for n in arr[:k])

    # 3. loop through arr and add the elements with at most 2 digits to output variable
    for i in range(k):
        # add the current element to the output variable if its number of digits is <= 2
        if len(str(arr[i])) <= 2:
            sum_of_k_digits += arr[i]

    return sum_of_k_digits

