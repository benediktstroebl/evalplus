
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

    # 1. make a new array
    # 2. for each value in arr, do the math and check if greater than 0
    # 3. return len of the new array

    count = 0
    newArr = []
    for x in arr:
        if sum(list(map(int, str(x)))) > 0:
            count += 1
    return count
