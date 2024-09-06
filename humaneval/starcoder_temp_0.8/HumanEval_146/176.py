
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odd_nums = [i for i in nums if i % 2!= 0]
    odd_nums = [i for i in odd_nums if i >= 10]
    odd_nums = [i for i in odd_nums if (i % 10) in [1, 3, 5, 7, 9]]
    odd_nums = [i for i in odd_nums if (i % 100) in [11, 13, 15, 17, 19]]
    odd_nums = [i for i in odd_nums if (i // 10) % 10 == 1]
    odd_nums = [i for i in odd_nums if (i // 100) % 10 == 1]
    return len(odd_nums)

