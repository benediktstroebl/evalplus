
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
    def is_positive_sum(n):
        if n == 0: return False
        if n < 0: n = -n
        return n % 10 > 0
    
    def get_sum(n):
        sum = 0
        while n > 0:
            sum += n % 10
            n //= 10
        return sum
    
    def rec(arr, index):
        if index >= len(arr): return 0
        if is_positive_sum(arr[index]):
            return 1 + rec(arr, index+1)
        else:
            return rec(arr, index+1)
    
    return rec(arr, 0)
    
    
