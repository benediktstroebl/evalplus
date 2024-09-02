
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
    def digit_sum(x):
        """Return the sum of the digits in the integer x."""
        return sum(int(d) for d in str(x))
    
    def count_positive_sum(arr):
        """Count the number of elements in the input array that have a sum of
        positive digits."""
        count = 0
        for num in arr:
            if digit_sum(num) > 0:
                count += 1
        return count
    
    return count_positive_sum(arr)