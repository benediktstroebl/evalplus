
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
    # Time: O(n)
    # Space: O(n)

    # Initialize the sum variable
    sum = 0

    # Iterate over the array
    for element in arr[:k]:
        # Get the digits of the element
        digits = len(str(element))

        # If the digits are less than or equal to 2, add the element to the sum
        if digits <= 2:
            sum += element

    return sum

