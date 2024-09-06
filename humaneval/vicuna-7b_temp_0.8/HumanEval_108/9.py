
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
    def count(n):
        if n < 0:
            n = abs(n)
        if n < 10:
            return 1
        else:
            for i in range(1, 10):
                if n % i == 0:
                    return 0
            return 1
    count_map = {10: 1, 9: 1, 8: 2, 7: 3, 6: 4, 5: 5, 4: 6, 3: 7, 2: 8, 1: 9}
    count_sum = 0
    for i in range(len(arr)):
        count = count(arr[i])
        count_sum += count
        count_nums[count] = count_sum
    return count_sum
