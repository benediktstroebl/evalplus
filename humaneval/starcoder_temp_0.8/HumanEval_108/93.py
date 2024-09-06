
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
    sum_num = 0
    counter = 0

    for element in arr:
        for digit in str(abs(element)):
            sum_num += int(digit)

        if sum_num > 0:
            counter += 1

        sum_num = 0

    return counter
