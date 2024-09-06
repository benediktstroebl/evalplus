
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    return sum(int(str(n)[0]=='1' or str(n)[-1]=='1') and int(str(n)[0]=='3' or str(n)[-1]=='3') and int(str(n)[0]=='5' or str(n)[-1]=='5') and int(str(n)[0]=='7' or str(n)[-1]=='7') and int(str(n)[0]=='9' or str(n)[-1]=='9') for n in nums)

