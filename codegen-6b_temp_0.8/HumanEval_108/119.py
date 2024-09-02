
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
    length = len(arr)
    for i in range(length):
        if i > 0:
            arr[i] += arr[i - 1]
    counter = 0
    for num in arr:
        single_digit = remove_sign(num)
        if num < 0:
            single_digit = single_digit * -1
        if len(str(single_digit)) > 1:
            counter += 1
    return counter

