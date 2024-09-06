
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

    def count_digits(num):
        if num == 0:
            return 1
        return 1 + count_digits(num // 10)

    def count_nums_helper(arr, cnt):
        if arr == []:
            return cnt

        num = arr[0]
        sign = num // abs(num)
        num = abs(num)

        if sign == 1:
            cnt += 1

        cnt += num % 10 > 0

        return count_nums_helper(arr[1:], cnt)

    return count_nums_helper(arr, 0)

