
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
    nums = set()
    for num in arr:
        nums.add(num)

    i = 0
    while i < 10:
        if (i not in nums) or (i < 0):
            i += 1
            continue
        j = 0
        flag = False
        while j < 10:
            if str(i) + str(j) in nums:
                flag = True
            j += 1
        if flag:
            i += 1
            continue
        else:
            return len(nums)

    return len(nums)

