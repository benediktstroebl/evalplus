
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
    def count_nums_helper(arr, idx):
        # base case
        if idx == len(arr):
            return 0
        # recursive step
        num = arr[idx]
        digit_sum = sum(map(int, str(abs(num))))
        if digit_sum > 0:
            return 1 + count_nums_helper(arr, idx + 1)
        else:
            return count_nums_helper(arr, idx + 1)
    return count_nums_helper(arr, 0)

