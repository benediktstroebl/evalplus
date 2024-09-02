
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
    sum_of_digits=0
    for number in arr:
        if(number<0):
            num_to_convert=number*(-1)
        else:
            num_to_convert=number
        while num_to_convert>0:
            sum_of_digits+=num_to_convert%10
            num_to_convert=num_to_convert//10
    if sum_of_digits>0:
        return 1
    return 0
