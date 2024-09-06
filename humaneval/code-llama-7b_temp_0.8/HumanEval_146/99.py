
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # NOTE: # Most people could come up with a solution like this:
    # num_greater_than_ten = len([x for x in nums if x > 10])
    # num_last_and_first_odd = len([x for x in nums if (x % 10 % 2 == 1) 
    # and (x / 10 % 2 == 1)])
    # return num_greater_than_ten + num_last_and_first_odd
    # This solution is relatively inefficient because it first creates 
    # 2 lists and then combines them.

    # It is more efficient to use a single list comprehension like this:
    return len([x for x in nums if x > 10 and (x % 10 % 2 == 1) 
    and (x / 10 % 2 == 1)])
    # More efficiency is gained by eliminating the % operations from the 
    # conditionals.
