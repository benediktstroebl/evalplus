
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

    out = 0
    for i in nums:
        if i > 10 and (int(str(i)[0])%2!= 0 or int(str(i)[-1])%2!= 0):
            out += 1
    return out

