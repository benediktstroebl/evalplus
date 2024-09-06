
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
    # 1. Return 0 if array is empty
    if arr == []:
        return 0
    # 2. Compare the numbers in the array
    count = 0
    for i in arr:
        # 3. Return 1 if number is positive
        if i > 0:
            count += 1
        # 4. Return 1 if number is negative
        elif i < 0:
            count += 1
        # 5. Return 0 if number is 0
    return count

