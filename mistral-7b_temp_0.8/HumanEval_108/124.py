
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
    # initialise count variable
    count = 0
    # loop through elements of array
    for i in range(len(arr)):
        # if the sum of digits of an element is greater than 0, then increment count variable
        if sum(int(j) for j in str(abs(arr[i])) if j != '-') > 0:
            count += 1

    return count

