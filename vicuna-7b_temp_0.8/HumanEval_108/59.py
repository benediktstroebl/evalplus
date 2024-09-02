
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
    # Find the sum of all digits
    sum_digits = 0
    for i in arr:
        if i < 0:
            sum_digits -= i
        else:
            sum_digits += i
    
    # Find the number of negative elements
    negative = 0
    for i in arr:
        if i < 0:
            negative += 1
    
    # Find the number of positive elements
    positive = 0
    for i in arr:
        if i > 0:
            positive += 1
    
    return positive + negative + sum_digits
