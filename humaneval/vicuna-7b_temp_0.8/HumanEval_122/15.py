
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
    # Use a dictionary to store the sum of digits for each k
    # Initialize the dictionary with zeros
    # Only need to use space to store the sum of digits for 1 <= i <= k
    # For i <= k, the sum of digits in arr[1:i] is the same as the sum of digits in arr[i:len(arr)]
    # So the maximum space required is len(arr)
    space = len(arr)
    # Use a dictionary to store the sum of elements for each k
    # Initialize the dictionary with zeros
    # For each k, the sum of elements in arr is the sum of digits of arr[1:k]
    # So the maximum space required is k
    sums = [0] * (k+1)
    # Initialize a list to store the sum of elements for each k
    result = []
    # Loop over all possible values of k
    for i in range(1, len(arr)):
        # Loop over all possible values of k
        for j in range(1, len(arr)):
            # Check if the two elements are less than or equal to k
            if j < i and j <= k:
                # Get the sum of the elements from the first k elements
                k_sum = sum_elements(arr, j)
                # Get the sum of the elements from the first k elements of the reversed array
                rev_arr = reversed(arr[j-1:])
                rev_k_sum = sum_elements(rev_arr, j-1)
                # Add the sum of the elements from the first k elements of the reversed array
                # to the sum of the elements from the first k elements of the original array
                result.append(k_sum + rev_k_sum)
                # Update the sum of elements for the current value of k
                sums[k] = k_sum + rev_k_sum
                # Update the sum of elements for the current value of k+1
                sums[k+1] = j
                # Update the space used
                space += j-1
                # If the value of k is greater than the current value of j
                # Update the result with the current value of j
                if j < k:
                    result.append(j
