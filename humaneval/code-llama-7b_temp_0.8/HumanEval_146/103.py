
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for number in nums:
        num = str(number)
        if len(num) >= 2 and (int(num[0]) % 2 != 0 and int(num[-1]) % 2 != 0) and (number > 10):
            count += 1
    return count

