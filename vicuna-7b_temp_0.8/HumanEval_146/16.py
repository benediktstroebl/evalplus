
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    if len(nums) == 0:
        return 0
    
    result = 0
    for num in nums:
        if num > 10 and (num % 1 if num % 1 == 0 else 0) and (num % 3 if num % 3 == 0 else 0) and (num % 5 if num % 5 == 0 else 0) and (num % 7 if num % 7 == 0 else 0) and (num % 9 if num % 9 == 0 else 0) == 1:
            result += 1
    return result
