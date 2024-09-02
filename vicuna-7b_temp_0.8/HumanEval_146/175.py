
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def isOdd(num):
        return num % 2 == 1
    
    def isFirstLastOdd(num):
        return isOdd(num[0]) and isOdd(num[-1])
    
    def check(num):
        if isOdd(num[0]) and isOdd(num[-1]):
            return True
        for i in range(1, len(num) - 1):
            if not isOdd(num[i]):
                return False
            if num[i] != num[i+1]:
                return False
        return True
    
    return len(filter(check, nums))
