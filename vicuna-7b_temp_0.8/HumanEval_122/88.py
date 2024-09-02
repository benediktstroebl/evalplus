
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
    # If len(arr) == 0 or len(arr) == k, return 0
    if len(arr) == 0 or len(arr) == k:
        return 0
    
    # Sort arr so that the first k elements are in ascending order
    arr = sorted(arr, reverse=True)
    
    # Initialize sum to 0
    sum = 0
    
    # Iterate over the first k elements of arr
    for i in range(k):
        # Get the current element of arr
        current = arr[i]
        
        # If current has at most two digits, add it to sum and increment k
        if len(current) <= 2:
            sum += current
            k += 1
        
    # Return sum
    return sum
