
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    # Solution 1
    # O(n) time complexity
    # O(1) space complexity
    # 17 chars
    # if not arr: return
    # p = 1
    # for x in arr: p *= -1 if x < 0 else 1
    # s = 0
    # for x in arr: s += p * x
    # return s

    # Solution 2
    # O(n) time complexity
    # O(1) space complexity
    # 17 chars
    # return sum([p * x for x in arr]) if len(arr) else None

    # Solution 3
    # O(n) time complexity
    # O(1) space complexity
    # 19 chars
    # return sum(arr) * (1 if not arr or abs(arr[0]) == arr[0] else -1) if len(arr) else None

    # Solution 4
    # O(n) time complexity
    # O(1) space complexity
    # 19 chars
    # if not arr: return
    # s, p = 0, 1
    # for x in arr: s += p * x; p *= -1 if x < 0 else 1
    # return s
