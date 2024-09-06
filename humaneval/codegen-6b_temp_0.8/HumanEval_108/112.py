
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
    # list off all the numbers
    # filter out all the numbers whose sum of digits is 0
    # then count the number of those

    # build up a count of all the numbers whose sum of digits is > 0
    # use a dictionary to keep track of the numbers
    # integer
    # count (dictionary)
        # key: number
        # value: count
    # loop of arr
    # if arr[i] > 0
    #   count += 1

    # return count

