
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def countOdd(num):
        odd = 0
        if num[-1] % 2 == 1 and num[0] % 2 == 1:
            odd += 1
        if num[-2] % 2 == 1 and num[-1] % 2 == 1:
            odd += 1
        return odd
    return sum([countOdd(num) for num in nums])