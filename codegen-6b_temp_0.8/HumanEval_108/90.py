
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
    cnt = 0
    for elem in arr:
        num = abs(elem)
        found = False
        while not found:
            if num == 0:
                break
            if num % 10 == 0:
                num = num // 10
                cnt = cnt + 1
            else:
                found = True
    return cnt

