
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
    "*** YOUR CODE HERE ***"
    num_count = 0
    for n in arr:
        if sum(map(lambda x: int(x), str(n))) > 0:
            num_count += 1
    return num_count
