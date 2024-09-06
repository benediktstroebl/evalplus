
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for number in nums:
        first_digit = number // 10 % 10
        last_digit = number % 10
        if first_digit + last_digit == 2:
            if first_digit >= 1 and first_digit <= 9 and last_digit >= 1 and last_digit <= 9:
                if number > 10:
                    count += 1
    return count
