
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

    numCounter = 0
    
    for num in nums:
        num = str(num)
        firstDigit = int(num[0])
        lastDigit = int(num[-1])
        if (firstDigit % 2!= 0) and (lastDigit % 2!= 0):
            numCounter += 1
    
    return numCounter
