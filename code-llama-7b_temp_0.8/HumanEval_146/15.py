
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    i = 0
    count = 0
    while i < len(nums):
        if len(str(nums[i])) < 2:
            i += 1
            continue
        if int(str(nums[i])[0]) % 2 != 0 and int(str(nums[i])[-1]) % 2 != 0 and nums[i] > 10:
            count += 1
        i += 1
    return count
