
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def check(n):
        """check if the first and last digits are odd"""
        first_digit = int(n / 10) % 10
        last_digit = n % 10
        return first_digit % 2 == 1 and last_digit % 2 == 1
    return len([n for n in nums if n > 10 and check(n)])

