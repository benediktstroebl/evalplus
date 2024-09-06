
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
    count = 0
    for num in arr:
        s = str(num)
        find_num = False
        for sign in range(len(s)):
            if find_num:
                break
            for i in range(len(s)):
                if int(s[sign:i]) > 0:
                    find_num = True
                    break
        if not find_num:
            count += 1
    return count

