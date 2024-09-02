
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

    # Reset the sum to 0
    sum = 0

    # Iterate over the array
    for num in arr:
        # If the number is less than 10
        if num < 10:
            # Increment the sum by num
            sum += num

        # If the number is less than 100
        if num < 100:
            # Increment the sum by num
            sum += num

        # If the number is less than 1000
        if num < 1000:
            # Increment the sum by num
            sum += num

        # If the k is equal to 0
        if k == 0:
            # Return the sum
            return sum

        # Decrement the k
        k -= 1

    # Return the sum
    return sum

