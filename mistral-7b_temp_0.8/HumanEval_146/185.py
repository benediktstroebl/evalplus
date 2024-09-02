
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
        if num < 10:
            continue
        elif str(num)[0] == "1" or str(num)[0] == "3" or str(num)[0] == "5" or str(num)[0] == "7" or str(num)[0] == "9":
            if str(num)[-1] == "1" or str(num)[-1] == "3" or str(num)[-1] == "5" or str(num)[-1] == "7" or str(num)[-1] == "9":
                count += 1
    return count
