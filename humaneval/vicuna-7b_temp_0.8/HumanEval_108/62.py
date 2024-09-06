
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
    # Write your code here
    
    # check if the list is empty
    if not arr:
        return 0
    
    # check if the last element of the list is positive
    last_pos = True
    last_digit = arr[-1]
    for i in range(len(arr)-1, -1, -1):
        if arr[i] < 0:
            last_pos = False
        elif arr[i] == last_digit:
            last_pos = False
        else:
            last_pos = True
    return last_pos
