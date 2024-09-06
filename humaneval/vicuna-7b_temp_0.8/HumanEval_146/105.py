
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # 1 <= num <= 10000
    count = 0
    for num in nums:
        first_dig = int(num[0])
        last_dig = int(num[-1])
        if first_dig % 2 == 1 and last_dig % 2 == 1 and num >= 10:
            count += 1
    return count

nums = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
result = specialFilter(nums)
