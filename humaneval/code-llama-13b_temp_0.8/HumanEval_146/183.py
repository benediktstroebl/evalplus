
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        num = str(num)
        first = int(num[0])
        last = int(num[-1])
        if (num.isdigit() and
            int(num) > 10 and
            first % 2 == 1 and
            last % 2 == 1):
            count += 1
    return count
