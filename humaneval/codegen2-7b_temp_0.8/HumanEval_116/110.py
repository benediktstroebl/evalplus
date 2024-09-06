
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
    count_ones = [0] * 10
    for num in arr:
        count_ones[bin(num).count('1')] += 1

    arr = arr.copy()
    for i in range(1, 10):
        for j in range(0, len(arr)):
            if count_ones[i] > count_ones[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count_ones[arr[j]] -= 1
                count_ones[arr[j+1]] -= 1
    return arr
    
