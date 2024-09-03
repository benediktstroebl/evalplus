def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    Returns None if the particular with negative numbers 
    """
    # initialize count of numbers with sum > 0 to 0
    c = 0
    for x in arr:
        sum_ = sum(map(int, str(x)))
        if sum_ > 0:
            c += 1
    return c
arr = [1,2,3,4,5,6]