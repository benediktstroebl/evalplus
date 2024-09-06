
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    first_half = []
    for i in range(len(nums) // 2):
        first_half.append(nums[i])
    second_half = []
    for i in range(len(nums) // 2, len(nums)):
        second_half.append(nums[i])
    nums = [first_half, second_half]
    count = 0
    for i in nums:
        for j in i:
            if j > 10:
                for k in range(len(str(j))):
                    if str(j)[k] == '1' or str(j)[k] == '3' or str(j)[k] == '5' or str(j)[k] == '7' or str(j)[k] == '9':
                        count += 1
    return count
