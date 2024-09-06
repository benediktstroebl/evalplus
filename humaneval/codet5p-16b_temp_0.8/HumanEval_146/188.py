
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

    numOdds = 0
    lastDigits = []
    for num in nums:
        lastDigits.append(num % 10)
        if num % 10 > 10:
            numOdds += 1
    firstOdds = False
    lastOdds = False
    if lastDigits[0] % 2 == 1:
        firstOdds = True
    if lastDigits[-1] % 2 == 1:
        lastOdds = True
    if numOdds == 0:
        return 0
    elif numOdds == 1:
        if firstOdds and lastOdds:
            return 1
    return numOdds

