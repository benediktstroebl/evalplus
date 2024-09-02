
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
    # count positive and negative numbers with same digit sum
    positive_count = 0
    negative_count = 0
    for x in arr:
        if x > 0:
            positive_count += 1
        else:
            negative_count += 1
    # count numbers with same digit sum as sum of arr
    digit_sum = sum(arr)
    count = 0
    for x in range(digit_sum):
        count += sum(arr[digit_sum - x - 1:])
    return positive_count + negative_count + count
