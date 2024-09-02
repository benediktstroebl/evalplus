
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    def specialFilterFunc(n):
        return str(n).startswith('1') and str(n).endswith('3') or str(n).startswith('3') and str(n).endswith('1') or str(n).startswith('5') and str(n).endswith('9') or str(n).startswith('7') and str(n).endswith('9') or str(n).startswith('9') and str(n).endswith('7')
    return len([x for x in nums if specialFilterFunc(x)])
