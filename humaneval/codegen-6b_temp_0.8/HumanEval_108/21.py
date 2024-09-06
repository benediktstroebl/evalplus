
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
    count_ = 0
    arr_ = arr[:]
    while arr_:
        first_num = arr_.pop()
        if first_num >= 0:
            count_ += 1
        else:
            first_num = abs(first_num)
            # last_num = arr_[-1]
            # arr_.pop()
            while first_num:
                digit = first_num % 10
                first_num //= 10
                if digit:
                    count_ += 1
                    # arr_.append(digit)
    return count_

