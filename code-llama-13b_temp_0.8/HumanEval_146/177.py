
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def checkOdd(num):
        return num % 2 == 1
    
    def checkFirstLast(num):
        return checkOdd(num[0]) and checkOdd(num[-1])

    def checkGreaterThan10(num):
        return num > 10

    total = 0
    for i in nums:
        strNum = str(i)
        if checkFirstLast(strNum) and checkGreaterThan10(i):
            total += 1
    return total
