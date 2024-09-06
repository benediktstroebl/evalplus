
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
    for num in arr:
        sum_ = 0
        num_string = str(num)
        for char in num_string:
            sum_ += int(char)
        sums.append(sum_)

    count = 0
    for sum_ in sums:
        if sum_ > 0:
            count += 1
    return count
