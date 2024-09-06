import math
def iscube(num):
    # If the input is negative, make it positive for easier handling
    if num < 0:
        num = -num

    # Calculating the cube of the integer square root of 'num'
    cube = int(math.sqrt(num)) ** 3

    # Comparing the calculated cube with the original input
    if cube == num:
        return True

    # If the conditions are not met, returning False indicating not a cube
    return False