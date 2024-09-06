
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    result = 0
    for i in nums:
        if i > 10:
            strI = str(i)
            if strI[0] == '1' or strI[0] == '3' or strI[0] == '5' or strI[0] == '7' or strI[0] == '9':
                if strI[len(strI) - 1] == '1' or strI[len(strI) - 1] == '3' or strI[len(strI) - 1] == '5' or strI[len(strI) - 1] == '7' or strI[len(strI) - 1] == '9':
                    result = result + 1
    return result
