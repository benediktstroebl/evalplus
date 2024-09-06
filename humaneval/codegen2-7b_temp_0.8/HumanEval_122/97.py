
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
    import itertools
    
    if arr:
        def add(a, b):
            return a + b if abs(a) <= 2 else a
        
        arr = list(map(int, str(sum(map(add, arr[:k], arr[k:])))))
        arr.sort(reverse=True)
        return ''.join(arr)
    else:
        return ''.join(['0']*k
