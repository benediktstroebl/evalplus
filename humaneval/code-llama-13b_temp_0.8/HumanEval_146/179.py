
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def firstOdd(num):
        if num % 10 % 2 != 0:
            return True
        return False

    def lastOdd(num):
        lastNum = str(num)[-1]
        if int(lastNum) % 2 != 0:
            return True
        return False

    def isGreaterThanTen(num):
        if num > 10:
            return True
        return False

    returnList = []
    for num in nums:
        first = firstOdd(num)
        last = lastOdd(num)
        greater = isGreaterThanTen(num)
        if first and last and greater:
            returnList.append(num)

    return len(returnList)

