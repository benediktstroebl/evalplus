
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odd_numbers = lambda n: 1 if n % 2 else 0
    odd_first_and_last_digits = lambda n: 0 if (odd_numbers(n%100 // 10) or odd_numbers(n % 10)) else 1
    return sum([1 for i in nums if i > 10 and odd_first_and_last_digits(i)])
