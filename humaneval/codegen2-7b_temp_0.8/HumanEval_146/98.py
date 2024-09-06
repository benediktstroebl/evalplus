
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    odd = []
    for i in nums:
        if (i < 0):
            break
        elif (i % 2 == 0 and i % 10 == 1):
            odd.append(i)
        elif (i % 2 == 1 and i % 10 == 3):
            odd.append(i)
        elif (i % 2 == 1 and i % 10 == 5):
            odd.append(i)
        elif (i % 2 == 1 and i % 10 == 7):
            odd.append(i
