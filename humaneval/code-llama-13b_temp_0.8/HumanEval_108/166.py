
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
    counter = 0
    for num in arr:
        if num > 0:
            counter += 1
        elif num < 0:
            num = -num
            while num > 0:
                digit = num % 10
                if digit > 0:
                    counter += 1
                    break
                num = int(num / 10)
    return counter

