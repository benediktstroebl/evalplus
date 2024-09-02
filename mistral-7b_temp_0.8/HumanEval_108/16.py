
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
    digits = {}
    for num in arr:
        if num < 0:
            num = num * -1
        if num >= 10:
            while num > 0:
                digit = num % 10
                digits[digit] = digits.get(digit, 0) + 1
                num = num // 10
    return len(digits.keys())
