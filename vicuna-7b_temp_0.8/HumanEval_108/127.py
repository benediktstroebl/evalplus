
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
    def count_sums(arr):
        sums = [sum(i) for i in arr]
        for x in sums:
            if x > 0:
                return x
        return 0
    
    def count_neg_sums(arr):
        sums = [sum(i) for i in arr]
        neg_sums = [sum(i) for i in arr]
        for x in neg_sums:
            if x < 0:
                return x
        return 0
    
    return count_sums(arr) + count_neg_sums(arr)