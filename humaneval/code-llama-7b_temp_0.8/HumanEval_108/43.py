
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
    def sign(n):
        return n // abs(n)
    
    def get_num_digits(n):
        digits = 0
        while n:
            n //= 10
            digits += 1
        return digits
    
    def count_recursive(arr, idx, sign, num_digits, count):
        if idx == len(arr):
            return count if sign * num_digits > 0 else 0
        
        n = arr[idx]
        return count_recursive(arr, idx + 1, sign, num_digits + get_num_digits(n),
                               count + 1)
    
    return count_recursive(arr, 0, sign(arr[0]), get_num_digits(arr[0]), 0)

