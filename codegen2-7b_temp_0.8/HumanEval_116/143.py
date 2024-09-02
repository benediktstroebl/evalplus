
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    if len(arr) == 1:
        return arr
    ans = []
    count_ones = 0
    for i in range(len(arr)):
        if arr[i] >= 0:
            count_ones += 1
        else:
            if count_ones > 0:
                ans.append(count_ones)
                count_ones = 0
    if count_ones > 0:
        ans.append(count_ones)
    ans += [0 for _ in range(len(arr)-len(ans))]
    ans.sort()
    return [x for x in arr if x == 0
