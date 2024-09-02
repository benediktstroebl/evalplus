
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
    # check if the number is a negative number
    if a < 0:
        # if it is a negative number, check if it is a cube of a positive number
        if a % 6 == 3:
            return True
        else:
            return False

    # if the number is positive, check if it is a cube of a prime number
    if a % 6 == 2:
        for i in range(6, 11):
            if a % i == 0:
                break
        if a % i == 0:
            return False
        else:
            return True

    # if the number is not divisible by 6, check if it is a cube of a number that is divisible by 3
    if a % 3 == 0:
        return True

    # if the number is not divisible by 3 and not divisible by 6, check if it is a cube of a number that is divisible by 2
    if a % 2 == 0:
        return True

    # if none of the above conditions are satisfied, return False
    return False
