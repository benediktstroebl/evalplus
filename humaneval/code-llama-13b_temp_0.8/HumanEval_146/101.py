
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def firstLastDigitCheck(x):
        str_x = str(x)
        return int(str_x[0]) % 2 == 1 and int(str_x[-1]) % 2 == 1
    
    nums_gt_10 = filter(lambda x: x > 10, nums)
    return len(list(filter(firstLastDigitCheck, nums_gt_10)))
