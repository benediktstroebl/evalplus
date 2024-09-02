
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
    sums = []
    for elem in arr:
        sum = 0
        while elem > 0:
            lastDigit = elem % 10
            sum += lastDigit
            elem = elem // 10
        sums.append(sum)
    # print(sums)
    if sums.count(0) != 0:
        return sums.count(0)
    return sums.count(0)
