
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    total = 0
    for i in range(len(nums)):
        if nums[i] > 10:
            if nums[i] // 10 == 1 or nums[i] // 10 == 3 or nums[i] // 10 == 5 or nums[i] // 10 == 7 or nums[i] // 10 == 9:
                if nums[i] % 10 == 1 or nums[i] % 10 == 3 or nums[i] % 10 == 5 or nums[i] % 10 == 7 or nums[i] % 10 == 9:
                    total += 1
    return total

