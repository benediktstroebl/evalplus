
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # Check the length of the array
    if len(nums) == 0:
        return 0
    
    # Check the last digit of the array
    last_digit = str(nums[-1])
    if last_digit[-1] % 2 != 0:
        return 0
    
    # Filter the numbers
    count = 0
    for num in nums:
        if num > 10 and (num % 2 != 0 or num % 3 != 0 or num % 5 != 0 or num % 7 != 0 or num % 9 != 0):
            count += 1
    return count
