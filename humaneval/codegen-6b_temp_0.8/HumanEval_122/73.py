
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
    counts = {}

    for num in arr[:k]:
        # initialize counts
        if num not in counts:
            counts[num] = 0

        counts[num] += 1

    # Combine all elements with k - 1 times
    for num in arr[k:]:
        # increment counts of existing numbers
        if num in counts:
            counts[num] += 1
        # initiate count for new numbers
        else:
            counts[num] = 1

    ans = 0
    for num, count in counts.items():
        if count <= 2:
            ans += num

    return ans

