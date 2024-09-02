
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    # Check if the input is a positive number
    if a > 0:
        # Check if it's a perfect cube
        if a ** 3 % 1 == 0:
            return True
        else:
            # Check if it's a cube of a prime number
            for i in range(1, a + 1):
                if a ** i % 1 == 0:
                    return True
            return False
    # Check if the input is negative
    elif a < 0:
        # Check if it's a perfect cube
        if a ** 3 % 1 == 0:
            return True
        else:
            # Check if it's a cube of a prime number
            for i in range(1, abs(a) + 1):
                if abs(a) ** i % 1 == 0:
                    return True
            return False
    # If the input is zero, it's a cube
    else:
        return True
