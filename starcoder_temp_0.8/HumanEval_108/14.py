
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
    for i in arr:
        a = []
        if i > 0:
            a = list(str(i))
            a = [int(j) for j in a]
            if sum(a) > 0:
                count += 1
        elif i < 0:
            a = list(str(i))
            a = [int(j) for j in a]
            a = a[1:]
            if sum(a) > 0:
                count += 1
    return count
