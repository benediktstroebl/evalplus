
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
    if not arr:
        return 0
    sum = 0
    for num in arr:
        sign = 0
        num = str(num)
        if num[0] < 0:
            num = "-" + num
            sign = -1
        result = sum + (num[1] if num[0] == "-" else num[1])
        while result != 0:
            sum += result % 10
            result = result / 10
    return sign * (len(arr) - 1 - (sum % 10))
