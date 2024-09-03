def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    The number is negative, then its first signed digit will be negative:
    e.g. -123 has a story1, 2, and 3
    """
    return sum(1 for num in arr if (num < 0 or abs(num) > 0))