
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
    def count_rec(arr, idx, cnt):
        if idx == len(arr):
            return cnt

        num = arr[idx]

        # if negative, then count all the following digits
        if num < 0:
            return count_rec(arr, idx + 1, cnt + len(str(num)) - 1)
        else:
            digits = list(map(int, str(num)))
            digit_sum = sum(digits)
            if digit_sum > 0:
                cnt += 1

            return count_rec(arr, idx + 1, cnt)

    return count_rec(arr, 0, 0)
