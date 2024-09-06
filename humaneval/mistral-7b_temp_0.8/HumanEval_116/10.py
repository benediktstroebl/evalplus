
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
    nums = []
    for x in arr:
        # Use binary() to convert a decimal number to a string of binary digits
        # The length of this string is the number of ones in the binary representation of x
        # x = int(binary(x)[::-1], 2)
        nums.append(x)
    return sorted(nums)



