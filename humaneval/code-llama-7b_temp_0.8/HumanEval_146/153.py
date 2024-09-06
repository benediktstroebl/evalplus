
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

    # a = 1 if nums[i] > 10 and nums[i][0] % 2 == 1 and nums[i][-1] % 2 == 1 else 0
    # return a
    # return sum(1 for num in nums if num > 10 and num % 10 % 2 != 0 and num // 10 % 2 != 0)
    # return len([num for num in nums if num > 10 and num % 10 % 2 != 0 and num // 10 % 2 != 0])

    return sum(1 for num in nums if num > 10 and int(str(num)[0]) % 2 == 1 and int(str(num)[-1]) % 2 == 1)

