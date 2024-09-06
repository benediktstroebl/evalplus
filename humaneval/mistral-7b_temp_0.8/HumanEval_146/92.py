
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

    def is_special(num):
        # your code here

        if (str(num) != ''):
            if (len(str(num)) == 1):
                if (num % 2 != 0):
                    return True
                else:
                    return False
            elif (len(str(num)) == 2):
                if (str(num)[0] % 2 != 0 or str(num)[1] % 2 != 0):
                    return True
                else:
                    return False
            elif (len(str(num)) == 3):
                if (str(num)[0] % 2 != 0 and str(num)[1] % 2 != 0 and str(num)[2] % 2 != 0):
                    return True
                else:
                    return False
            elif (len(str(num)) == 4):
                if (str(num)[0] % 2 != 0 and str(num)[1] % 2 != 0 and str(num)[2] % 2
