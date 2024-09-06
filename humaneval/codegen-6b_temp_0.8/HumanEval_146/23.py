
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def is_odd(num):
        return num % 2 == 1

    def has_odd_digit(num):
        return is_odd(num // 10) and is_odd(num % 10)

    return sum(has_odd_digit(num) for num in nums)

