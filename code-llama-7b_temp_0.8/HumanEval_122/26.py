
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
    def sum_elements(arr):
        result = 0
        for n in arr:
            result += n
        return result

    def remove_elements(arr, k):
        for i in range(k):
            arr.pop(0)

    def number_of_digits(n):
        digits = 0
        while n:
            digits += 1
            n //= 10
        return digits

    result = sum_elements(arr[:k])
    remove_elements(arr, k)

    for i in range(k, len(arr)):
        if number_of_digits(arr[i]) > 2:
            break
        result += arr[i]
        remove_elements(arr, 1)

    return result


