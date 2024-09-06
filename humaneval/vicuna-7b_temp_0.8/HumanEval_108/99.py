
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
    # If there are no numbers in the input array, the function should return 0.
    if not arr:
        return 0

    # Initialize a variable to count the number of positive numbers.
    positive = 0

    # Iterate through the input array.
    for num in arr:
        # If the number is negative, subtract it from the positive variable.
        if num < 0:
            positive -= num
        # If the number has a positive sign, add it to the positive variable.
        else:
            positive += num

    return positive
