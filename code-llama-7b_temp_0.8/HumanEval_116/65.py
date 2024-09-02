
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
    nums_1s = [num for num in arr if bin(num).count("1") == 1]
    nums_2s = [num for num in arr if bin(num).count("1") == 2]
    nums_3s = [num for num in arr if bin(num).count("1") == 3]
    nums_4s = [num for num in arr if bin(num).count("1") == 4]
    nums_5s = [num for num in arr if bin(num).count("1") == 5]
    nums_6s = [num for num in arr if bin(num).count("1") == 6]
    nums_7s = [num for num in arr if bin(num).count("1") == 7]
    nums_8s = [num for num in arr if bin(num).count("1") == 8]
    nums_9s = [num for num in arr if bin(num).count("1") == 9]
    nums_10s = [num for num in arr if bin(num).count("1") == 10]
    nums_11s = [num for num in arr if bin(num).count("1") == 11]
    nums_12s = [num for num in arr if bin(num).count("1") == 12]
    nums_13s = [num for num in arr if bin(num).count("1") == 13]
    nums_14s = [num for num in arr if bin(num).count("1") == 14]
    nums_15s = [num for num in arr if bin(num).count("1") == 15]
    nums_16s = [num for num in arr if bin(num).count("1") == 16]
    nums_17s = [num for num in arr if bin(num).count("1") == 17]
    nums_18s = [num for num in arr if bin(num).count("1") == 18]
    nums_19s =
