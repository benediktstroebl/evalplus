
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
    # Set to track all unique values
    unique = set()
    # Set to track all unique digits in each number
    digits = set()
    # For each number in array
    for num in arr:
        # If number has 2 digits
        if len(str(num)) <= 2:
            # Add all digits to set
            for digit in str(num):
                digits.add(digit)
            # Add number to set of unique values
            unique.add(num)
    # For each unique digit in set
    for digit in digits:
        # Add it to the sum
        sum_ = sum([int(digit) for num in unique if len(str(num)) <= 2 and digit in str(num)])
    # Return sum
    return sum_
