
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
    def get_sum(i):
        """
        Function to return the sum of the elements in arr
        with at most two digits starting from the index i
        """
        # Initialize the sum to 0
        total = 0

        # Loop through the elements starting from i
        # and add the elements to the sum
        for j in range(i, i + 2):
            # Check if the element is in the allowed range
            # and add it to the sum
            if 10 <= arr[j] <= 99:
                total += arr[j]
        return total

    # Loop through the first k elements
    for i in range(k):
        # Add the sum of the elements with at most two digits
        # to the sum
        total += get_sum(i)

    return total
