
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
    result = 0
    for x in arr:
        # Take the absolute value of x.
        x_abs = abs(x)
        # x_abs's sum of digits is 0.
        if x_abs == 0:
            result += 1
            continue
        # x_abs's sum of digits is > 0.
        else:
            # Store the sum of digits.
            digit_sum = 0
            # Traverse each digit.
            while x_abs > 0:
                digit = x_abs % 10
                digit_sum += digit
                # Move to the next digit.
                x_abs = x_abs // 10
            if digit_sum > 0:
                result += 1
    return result
