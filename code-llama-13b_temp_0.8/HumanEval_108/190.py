
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    count = 0

    # Go through all the elements
    for num in arr:
        # If the number is negative, multiply it by -1
        if num < 0:
            num *= -1

        # Keep dividing the number by 10 until it's less than 10
        while num >= 10:
            num = num // 10

        # If it's greater than 0, then count it
        if num > 0:
            count += 1

    return count

