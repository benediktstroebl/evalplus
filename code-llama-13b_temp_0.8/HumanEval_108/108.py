
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

    # make a copy of the list since we are going to change it
    nums = arr.copy()

    # initialize the counter
    cnt = 0

    # loop through the array
    for i in range(len(nums)):
        # split the number into its digits
        digits = str(nums[i])

        # we only need to check the first digit
        if int(digits[0]) > 0:
            cnt += 1

    # return the counter
    return cnt

