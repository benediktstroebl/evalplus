
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
    # Create a set for the k elements
    set = set(arr[:k])

    # Initialize the sum to 0
    sum = 0

    # Iterate over each element in arr and add it to the sum if it has at most two digits
    for num in arr:
        if len(str(num)) <= 2:
            sum += num

    return sum
