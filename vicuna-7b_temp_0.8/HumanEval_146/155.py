
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    # I have to write a new list to store the filtered numbers
    filtered_nums = []
    # I have to use a for loop to iterate through the input list
    for num in nums:
        # I have to check the first and last digits separately
        if (num[0] % 2 == 0 and num[-1] % 2 == 0) or ((num[0] % 2 == 1 and num[-1] % 2 == 1)) or (num[0] % 2 == 3 and num[-1] % 2 == 3) or (num[0] % 2 == 5 and num[-1] % 2 == 5) or (num[0] % 2 == 7 and num[-1] % 2 == 7) or (num[0] % 2 == 9 and num[-1] % 2 == 9):
            filtered_nums.append(num)
    return len(filtered_nums)
