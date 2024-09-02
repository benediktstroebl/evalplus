
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
    # O(n) where n = length of arr
    # O(1) space
    
    # handle edge case of empty array
    if len(arr) == 0:
        return 0
    # init sum counter
    num_sums = 0
    
    # loop through array
    for i in range(len(arr)):
        # init sum of digits
        num_sum = 0
        # get number
        num = arr[i]
        # check if number is negative
        if num < 0:
            num = -num
        # get length of number
        num_len = len(str(num))
        # for each digit in number
        for j in range(num_len):
            # sum digits
            num_sum += int(num[j])
        # check if sum of digits is greater than 0
        if num_sum > 0:
            num_sums += 1
    # return number of positive summed digits
    return num_sums

