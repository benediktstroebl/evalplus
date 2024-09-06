
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
    for i in range(len(arr)):
        sum_digits = 0
        number = arr[i]
        if number < 0:
            number = number * -1

        while number > 0:
            sum_digits = sum_digits + (number % 10)
            number = number // 10

        if sum_digits > 0:
            count = count + 1

    return count
