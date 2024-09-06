
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odd = [1,3,5,7,9]
    counter = 0
    for num in nums:
        first_digit = num % 10
        last_digit = num / 10
        if num > 10:
            if first_digit in odd and last_digit in odd:
                counter += 1
    return counter
