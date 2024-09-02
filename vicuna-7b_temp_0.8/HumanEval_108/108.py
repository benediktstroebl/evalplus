
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
    def count_helper(arr):
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                num = arr[i] + arr[j]
                if num > 0:
                    count += num
                    break
        return count
    return count_helper(arr)
