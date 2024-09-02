
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
    # Step 1: Extract the first k elements from the array
    first_k = arr[:k]
    # Step 2: Find the number of digits in each element
    digits = [len(str(num)) for num in first_k]
    # Step 3: Find how many elements with 1 or 2 digits there are in the first k elements
    two_digits = len(list(filter(lambda x: x < 3, digits)))
    # Step 4: Find the sum of the numbers with 1 or 2 digits
    return sum(first_k[:two_digits])


