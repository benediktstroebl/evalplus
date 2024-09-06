
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    oddNumber = 0
    oddNumber10 = 0
    i = 0

    while i < len(nums):
        # convert number to string
        stringNum = str(nums[i])
        # check if the first and last digits are odd
        if stringNum[0] % 2 == 1 and stringNum[1] % 2 == 1:
            oddNumber10 += 1
            # check if the number is greater than 10
            if nums[i] > 10:
                oddNumber += 1
        i += 1

    return oddNumber10 + oddNumber

