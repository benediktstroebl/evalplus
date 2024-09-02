
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
        if isinstance(num, int):
            num = abs(num)
            while num > 0:
                digit = num % 10
                num //= 10
                if digit > 0:
                    count += 1
        elif isinstance(num, float):
            num = abs(num)
            num_str = str(num)
            num_len = len(num_str)
            for i in range(num_len):
                digit = int(num_str[i])
                if digit > 0:
                    count += 1
    return count
