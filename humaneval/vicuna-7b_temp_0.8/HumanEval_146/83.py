
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def process(num):
        digit1, digit2 = map(int, str(num)[::2])
        if (digit1 - digit2) % 2 == 0:
            return False
        return digit1 % 2 == 1 and digit2 % 2 == 1 and num > 10
    return sum(1 for num in nums if process(num))
