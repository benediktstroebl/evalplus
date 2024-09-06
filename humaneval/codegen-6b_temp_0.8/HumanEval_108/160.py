
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
    count = 0
    for num in arr:
        if abs(num) < 10:
            count += 1
        else:
            last_digit = abs(num) % 10
            if last_digit == 0:
                continue
            elif last_digit > 0:
                if last_digit > 1:
                    count += 1
            else:
                first_digit = abs(num) // 10
                if first_digit * 10 - abs(num) == -1:
                    count += 1
    return count

