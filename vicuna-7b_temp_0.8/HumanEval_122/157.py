
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
    # Create an empty list to store the sum
    sum = []
    # Loop through the first k elements of arr
    for i in range(k):
        # Add the current element to the sum
        sum.append(arr[i])
        # Remove the current element from the list
        arr.remove(arr[i])
    # Join the remaining elements to the sum list
    sum = sum[:-1]
    # Return the sum
    return sum[::-1]