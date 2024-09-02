
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
    def get_twosum(arr, k, index):
        index += index
        left = min(index - k, 0)
        right = max(index + k, len(arr) - 1)
        while left < right:
            if arr[left] + arr[right] == target:
                return True
            elif arr[left] + arr[right] < target:
                left += 1
            else:
                right -= 1
        return False

    if len(arr) <= k:
        return sum(arr)

    arr.sort()
    target = arr[k - 1]
    for i in range(k - 1, len(arr) - k):
        if not get_twosum(arr, k, i):
            return target

