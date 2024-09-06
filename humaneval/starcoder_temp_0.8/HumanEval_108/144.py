
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
    # Your code here
    if len(arr) == 0:
        return 0
    else:
        count = 0
        for i in range(len(arr)):
            sum = 0
            arr[i] = abs(arr[i])
            while arr[i] > 0:
                r = arr[i] % 10
                sum += r
                arr[i] = arr[i] // 10
            if sum > 0:
                count += 1
        return count

