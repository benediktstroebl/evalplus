
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # create a counter
    counter = 0
    # loop through nums
    for num in nums:
        # check if first and last digits are odd and greater than 10
        if num%10 != 0 and num%100 != 0 and num > 10:
            # if they are add to the counter
            counter += 1
    return counter
