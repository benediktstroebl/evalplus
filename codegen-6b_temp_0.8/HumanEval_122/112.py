
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
    # let's save some time by checking for empty arrays
    if not arr:
        return 0

    # this will be the subarray we're going to work with
    subarray = arr[:k]

    # this tells us how many unique digits we have
    unique_digits = len(set(str(el) for el in subarray))

    # this will tell us how many non-unique digits we have
    non_unique_digits = len(subarray) - unique_digits

    # we're adding the unique digits * k, non-unique digits * k,
    # and just the non-unique digits
    return unique_digits * k + non_unique_digits * k

