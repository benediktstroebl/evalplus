
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
    num_positive = 0
    for num in arr:
        digit_sum = 0
        if num >= 0:
            for digit in str(num):
                digit_sum += int(digit)
        else:
            first_digit = num//(10**(len(str(num))-1))
            digit_sum = abs(first_digit)
            for digit in str(abs(num)):
                digit_sum += int(digit)
        if digit_sum > 0:
            num_positive += 1
    return num_positive

