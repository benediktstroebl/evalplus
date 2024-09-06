
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
    # 2015/07/23 - Improve the code with bit manipulation
    n = len(arr)
    nums_with_sum_of_digits_gt_0 = 0
    for i in range(n):
        bits = [int(d) for d in arr[i]]
        num_with_sum_of_digits_gt_0 = sum(int(d) for d in bits)
        nums_with_sum_of_digits_gt_0 += abs(num_with_sum_of_digits_gt_0)
    return nums_with_sum_of_digits_gt_0

print(count_nums([-1, 11, -11]))
print(count_nums([1, 1, 2]))