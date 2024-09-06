
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
    def helper(arr):
        if not arr:
            return 0
        count = 0
        for num in arr:
            if str(num) != '-':
                count += 1
            else:
                sign = int(num[1]) if num[1] in '1234567890' else 1
                num = int(num[:-2])
                count += helper(num + [sign])[0]
        return count
    return helper(arr)
