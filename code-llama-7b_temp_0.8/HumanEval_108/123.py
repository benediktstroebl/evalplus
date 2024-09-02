
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
    total = 0
    for i in arr:
        print(i)
        if i < 0:
            nums = str(i)[1:]
            #print(nums)
            total_nums = 0
            for n in nums:
                total_nums = total_nums + int(n)
                print(total_nums)
            if total_nums > 0:
                total += 1
        elif i > 0:
            nums = str(i)
            #print(nums)
            total_nums = 0
            for n in nums:
                total_nums = total_nums + int(n)
                #print(total_nums)
            if total_nums > 0:
                total += 1
    return total

