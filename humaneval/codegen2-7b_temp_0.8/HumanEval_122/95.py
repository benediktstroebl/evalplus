
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
    def func(arr, k):
        i = 0
        while i < len(arr):
            if len(str(arr[i])) > 2:
                arr[i] = str(arr[i])
                i += 1
                continue
            if i + k > len(arr):
                break
            s = arr[i:i+k]
            if len(s) < 2:
                break
            s = int(''.join(s))
            arr[i] = s
            i += 1

        return sum(arr)

    
