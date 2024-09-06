
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
    # Write your code here
    result = 0
    for i in arr:
        if i < 0:
            sign = -1
        else:
            sign = 1
        result += sum(map(int, [abs(digit) for digit in str(i)]))
    return result
