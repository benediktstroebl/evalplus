
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
    if a**3 == a:
        return True
    else:
        return False

    if iscube(int(a)):
        print(f"{a} is a cube of {int(a)}")
    else:
        print(f"{a} is not a cube of {int(a)}")
    a = input("Enter a number: ")
    
