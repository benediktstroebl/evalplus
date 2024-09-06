
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
    # create a set to store unique pairs
    pairs = set()
    for i in range(k):
        # iterate through first k elements
        # get first and second digits
        first_digit = arr[i] // 10
        second_digit = arr[i] % 10
        # add the pair to the set
        pair = (first_digit, second_digit)
        pairs.add(pair)
    # count the total number of unique pairs
    total = len(pairs)
    # iterate through the rest of the array
    for i in range(k, len(arr)):
        # get first and second digits
        first_digit = arr[i] // 10
        second_digit = arr[i] % 10
        # remove the pair from the set
        pair = (first_digit, second_digit)
        pairs.remove(pair)
        # add the pair to the set
        pairs.add((second_digit, first_digit))
        # increment total
        total += 1
    return total
