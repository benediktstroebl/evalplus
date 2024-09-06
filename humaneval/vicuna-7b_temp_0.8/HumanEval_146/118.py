
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    return sum(filter(lambda x: x > 10 and str(x)[0] % 2 != str(x)[1] % 2 and abs(int(str(x)[0]) - int(str(x)[1])) % 2 == 1 and x % 10 == 1 or x % 10 == 3 or x % 10 == 5 or x % 10 == 7 or x % 10 == 9 and x < 1000 for x in nums))