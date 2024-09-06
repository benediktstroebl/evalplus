
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for i in range(0, len(nums)):
        # first check the last digit
        lastDigit = int(str(nums[i])[-1])
        if lastDigit % 2 != 0:
            # then check the first digit
            firstDigit = int(str(nums[i])[0])
            if firstDigit % 2 != 0:
                # then check if the number is greater than 10
                if nums[i] > 10:
                    # if it's all true, increase the count
                    count += 1
    return count
