
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
    # Get the digits from left to right
    digits = [arr[i:i+1] for i in range(len(arr) - k + 1)]
    # Initialize the sum to 0
    s = 0
    # Iterate over each digit
    for d in digits:
        # If the length of the digit is 1, it should be ignored
        if len(d) == 1:
            continue
        # If the length of the digit is 2, add the element and update the sum
        if len(d) == 2:
            s += d[0]
            s += d[0]
        else:
            # Otherwise, add the digits by adding their values in base 10
            # Ignore the leading zeros
            s += sum(int(digit) for digit in d)
    return s
