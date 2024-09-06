
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    oddDigits = [i for i in nums if i % 2 != 0]
    firstLastOdd = [i[0] for i in oddDigits if i[-1] % 2 == 1]
    result = len(firstLastOdd)
    for num in oddDigits:
        if num > 10:
            result -= 1
    return result
