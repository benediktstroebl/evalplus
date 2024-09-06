
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
    # IMPORTANT: UNDERSTAND the PROBLEM FIRST
    # HINT: Write Out in English the Steps of the Hinted Solution
    # FORMULATE Abbreviations
    # DO NOT OVERCOMPLICATE
    # FORGET ABOUT PREMATURE OPTIMIZATION

    # RESULTS
    # Runtime: 72ms
    # Memory: 14.3MB

    return sum(x for x in arr[:k] if len(str(x)) <= 2)

    # RESULTS
    # Runtime: 72ms
    # Memory: 14.2MB

    # return sum(x for x in arr[:k] if len(str(x)) <= 2)

    # RESULTS
    # Runtime: 160ms
    # Memory: 14.2MB

    # return sum(
    #     x for x in arr[:k]
    #     if len(str(x)) <= 2
    # )
