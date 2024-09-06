
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
    nums = []
    for i in range(len(arr)):
        count = 0
        if arr[i] >= 0:
            sum_of_digits = 0
            while arr[i] > 0:
                sum_of_digits += arr[i]%10
                arr[i] //= 10
            if sum_of_digits > 0:
                nums.append(arr[i])
        elif arr[i] < 0:
            sum_of_digits = 0
            while arr[i] > 0:
                sum_of_digits += (arr[i]*-1)%10
                arr[i] = -1 * (arr[i]//10)
            if sum_of_digits > 0:
                nums.append(arr[i])
    return len(nums)
