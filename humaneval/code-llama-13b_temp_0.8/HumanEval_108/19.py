
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
    # ====================================
    # Do not change the code before this

    # ====================================
    # Write your code here
    # count = 0
    # for number in arr:
    #     number = str(number)
    #     total = 0
    #     for digit in number:
    #         total += int(digit)
    #     if total > 0:
    #         count += 1

    # return count
    count = 0
    for num in arr:
        if num > 0:
            count += 1
        elif num < 0:
            total = -num
            while total > 0:
                total -= total % 10
                total //= 10
            if total > 0:
                count += 1
    return count

    # ====================================
    # Do not change the code after this
    return nums
