
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
    visited = set()
    i = 0

    while i < k:
        val = arr[i]
        if re.search(r'\d{2}', str(val)):
            visited.add(val)
        i += 1

    i = 0

    while i < len(arr):
        val = arr[i]
        if val not in visited:
            visited.add(val)
        i += 1

    return sum(visited)

