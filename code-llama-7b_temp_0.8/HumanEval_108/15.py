
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
    # create a cache dict:
    # key: current sum
    # value: number of elements that have this sum
    cache = {}
    # create a counter that is the number of elements that have a sum > 0
    num_with_sum_over_0 = 0
    # iterate through all elements in the array
    for num in arr:
        # if the number is negative, count as negative
        if num < 0:
            current_sum = num
        # if the number is positive, count as positive
        else:
            current_sum = 0
        # iterate through all the digits of the current number
        for digit in str(abs(num)):
            current_sum += int(digit)
            # if the current sum is a key in the cache, add 1 to the value for that key
            if current_sum in cache:
                cache[current_sum] += 1
            # otherwise, create a new key
            else:
                cache[current_sum] = 1
        # if the current sum is greater than 0, increment the number of elements with sum > 0
        if current_sum > 0:
            num_with_sum_over_0 += 1
    # return the number of elements with a sum > 0
    return num_with_sum_over_0
