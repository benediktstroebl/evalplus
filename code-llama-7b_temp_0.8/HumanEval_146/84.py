
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # if len(nums) == 0:
    #     return 0
    # newNum = []
    # for i in range(len(nums)):
    #     if (nums[i] > 10 and nums[i] % 10 in (1, 3, 5, 7, 9) and nums[i] // 10 % 2 == 1):
    #         newNum.append(nums[i])
    # return len(newNum)

    if len(nums) == 0:
        return 0
    else:
        newNum = []
        for i in nums:
            if (i > 10 and i % 10 in (1, 3, 5, 7, 9) and i // 10 % 2 == 1):
                newNum.append(i)
        return len(newNum)
