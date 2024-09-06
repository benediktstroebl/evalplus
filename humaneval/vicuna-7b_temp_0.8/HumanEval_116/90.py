
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
    n = len(arr)
    if n == 0:
        return [0]
    else:
        # binary representation of n
        binary = [0] * (n + 1)
        for i in range(n):
            binary[i] = 1
        # move 1 to left, 0 to right
        for i in range(n - 1, 0, -1):
            binary[i] = binary[i - 1] + binary[i]
            # check number of ones in binary
            count = 0
            for j in binary:
                if j == 1:
                    count += 1
            # compare with previous elements
            if count > arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        # sort remaining elements
        for i in range(n):
            for j in range(i + 1, n):
                if arr[j] > arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
    return arr