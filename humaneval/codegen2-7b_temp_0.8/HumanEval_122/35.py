
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
    def sum_digits(num):
        return sum(int(i) for i in str(num))

    result = 0
    count = 0
    for i in arr[:k]:
        if count == 2:
            break
        result += i
        count += 1
    return result + sum(arr[k:])

