
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
    total_num = 0
    for number in arr:
        number = abs(number)
        if len(str(number)) > 1:
            number = int(str(number)[0])
            if number < 0:
                number = number * -1
            total_num += number
    return total_num

