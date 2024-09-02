
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
    # Convert the number to the float format
    float_num = float(a)
    # Raise the number to the 1/3
    answer = float_num ** (1/3)
    # Floor of the answer to make sure that there is no decimal number
    answer = math.floor(answer)
    # Check if the answer is a cube
    if answer ** 3 == a:
        return True
    return False
