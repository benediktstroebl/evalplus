
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
    # 1. Add all elements with len <= 2
    # 2. Add the elements with len == 3 if k >= len(arr) - 3
    # 3. Add (k - (arr len - 3)) to the sum

    # 1. Add all elements with len <= 2
    total = 0
    for el in arr[:k]:
        if el <= 99:
            total += el

    # 2. Add the elements with len == 3 if k >= len(arr) - 3
    if k >= len(arr) - 3:
        for el in arr[k - len(arr) + 3:]:
            if el <= 99:
                total += el

    # 3. Add (k - (arr len - 3)) to the sum
    else:
        total += sum(arr[k - len(arr) + 3:k])

    return total

