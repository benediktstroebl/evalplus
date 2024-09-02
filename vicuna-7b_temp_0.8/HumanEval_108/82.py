
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
    # Use a dictionary to count the number of positive integers with each sum
    num_count = {}
    for i in arr:
        key = sum(str(digit) for digit in i)
        if key in num_count:
            num_count[key] += 1
        else:
            num_count[key] = 1

    # Count the number of negative integers
    negative = [digit for digit in arr if digit < 0]
    return len(negative)
