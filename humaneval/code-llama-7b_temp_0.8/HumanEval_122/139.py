
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
    """
    Time: O(n) - where n is the len(arr)
    Space: O(1) - assuming "sum" takes O(1) to concatenate string of two digits
    """
    def concat(num1, num2):
        return str(num1) + str(num2)

    sum = 0
    arr_len = len(arr)
    for i in range(min(k, arr_len)):
        nums = arr[i: i + 2]
        num = concat(nums[0], nums[1]) if len(nums) > 1 else nums[0]
        sum += num
    return sum

    # return sum([int(num) for num in str(sum(arr[:k]))])

