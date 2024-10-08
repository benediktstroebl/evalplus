
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
    if len(arr) == 0:
        return 0
    nums_with_positive_digitsum = 0
    for num in arr:
        num_with_positive_digitsum = False
        if num > 0:
            num_with_positive_digitsum = True
        elif num < 0:
            num = abs(num)
            for i in range(1, len(str(num)) + 1):
                if int(str(num)[-i]) > 0:
                    num_with_positive_digitsum = True
                    break
        if num_with_positive_digitsum:
            nums_with_positive_digitsum += 1
    return nums_with_positive_digitsum
