
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
    # Check if the array is empty
    if not arr:
        return 0
    
    # Create an empty list to store the count
    count = [0]
    
    # Loop through the array and count the numbers
    for num in arr:
        # Check if the number is negative
        if num < 0:
            # If the number is negative, the first digit must be negative
            num = -num
        # Check if the number has a positive sum of its digits
        while num > 0:
            count[count.index(num)] += 1
            num = num / 10
    
    # Return the count
    return count[0]
