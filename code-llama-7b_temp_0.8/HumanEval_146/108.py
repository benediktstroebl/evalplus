
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odd_number = lambda n: (n % 2 == 1)
    check_10_digit = lambda n: (abs(n) % 10 == 0)
    count = 0
    for num in nums:
        if (num > 10) and (odd_number(num) and check_10_digit(num)):
            count += 1
    return count
