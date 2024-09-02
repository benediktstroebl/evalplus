
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
    def sum_digits(num):
        sum_digit = 0
        if num < 0:
            num = -num
            sum_digit -= 1
        while num > 0:
            sum_digit += num % 10
            num = num // 10
        return sum_digit
    
    count = 0
    for i in arr:
        if sum_digits(i) > 0:
            count += 1
    return count
