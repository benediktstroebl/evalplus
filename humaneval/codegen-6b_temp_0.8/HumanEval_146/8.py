
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for n in nums:
        first_digit = n / 100
        second_digit = n % 100
        if first_digit == 1 or second_digit == 1 or first_digit == 3 or second_digit == 3 or first_digit == 5 or second_digit == 5 or first_digit == 7 or second_digit == 7 or first_digit == 9 or second_digit == 9:
            if n > 10 and (first_digit % 2 != 0 or second_digit % 2 != 0):
                count += 1 
    return count 
        
