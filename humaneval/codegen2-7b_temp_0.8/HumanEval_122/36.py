
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
    for i in range(k):
        nums = [int(e) for e in str(arr[i])]
        for j in range(1, len(nums)):
            if nums[j] > 9:
                nums[j] -= 10
                nums[j - 1] += 1
        arr.append("".join([str(e) for e in nums[:2]]))
    return int("".join([str(e) for e in arr[k:]]))

