
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
    def count_first_digit(arr, num):
        result = 0
        if num >= 0:
            result += 1
        else:
            result += 1 - (num % 10)

        return result

    def count_nums_helper(arr, num):
        if len(arr) == 0:
            return count_first_digit(arr, num)

        if count_first_digit(arr, num) == 0:
            return count_nums_helper(arr[1:], num * 10 + arr[0])
        else:
            return count_nums_helper(arr[1:], num * 10 + arr[0]) + 1

    return count_nums_helper(arr, 0)

