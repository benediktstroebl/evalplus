
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

    if len(arr) < 2:
        return sum(arr)

    # Step 1.
    # Sort the array
    arr.sort()

    # Step 2.
    # Iterate over the first k elements
    # Add the elements to the result
    result = 0
    for i in range(k):
        result += arr[i]

    # Step 3.
    # Set the variables
    n_digits = 1
    i = 0
    j = k
    num = 0

    # Step 4.
    # Iterate over the remaining elements
    while j < len(arr):
        # Add the digits to the num
        num = num * 10 + arr[j]

        # If we have already seen 2 digits, then add num to result
        if n_digits == 2:
            result += num

        # Increment the variables
        n_digits += 1
        i += 1
        j += 1

        # Reset num if n_digits > 2
        if n_digits > 2:
            num = 0
            n_digits = 1

    return result

