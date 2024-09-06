
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
    def is_positive(x):
        x = str(x)
        for c in x:
            if int(c) >= 0:
                return True
        return False

    arr_new = []
    for num in arr:
        sum_of_digits = 0
        x = str(num)
        for c in x:
            sum_of_digits += int(c)
        if is_positive(sum_of_digits) == True:
            arr_new.append(num)
    return len(arr_new)

