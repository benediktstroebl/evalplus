
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """

    if x % 2!= 0 or y % 2!= 0: # If x and y aren't even numbers
        return -1
    else:
        for num in range(x, y+1): # Iterate through all numbers
            if num % 2 == 0: # If num is even
                return num # Return the biggest even number
