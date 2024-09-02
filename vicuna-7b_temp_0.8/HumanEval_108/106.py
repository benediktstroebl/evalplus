
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
    nums = set(arr)
    for num in nums:
        for i in range(len(num)):
            for j in range(len(num)):
                if i == j:
                    continue
                if num[i] > 0 and num[j] > 0 and (num[i] + num[j]) % 10 > 0:
                    count += 1
    return count