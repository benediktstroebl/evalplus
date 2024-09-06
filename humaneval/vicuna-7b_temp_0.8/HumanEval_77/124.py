
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
    # 1. Check if a is a cube of 1
    if a == True:
        return True
    
    # 2. Check if a is a cube of 2
    if a % 2 == 0:
        if a % 2 == 0 and a % 2 == 1:
            return True
        elif a % 2 == 0 and a % 2 == 0:
            return True
    
    # 3. Check if a is a cube of 3
    if a % 3 == 0:
        if a % 3 == 0 and a % 3 == 1:
            return True
        elif a % 3 == 0 and a % 3 == 2:
            return True
        elif a % 3 == 1 and a % 3 == 2:
            return True
        
    # 4. Check if a is a cube of 4
    if a % 4 == 0:
        if a % 4 == 0 and a % 4 == 1:
            return True
        elif a % 4 == 0 and a % 4 == 2:
            return True
        elif a % 4 == 0 and a % 4 == 3:
            return True
        elif a % 4 == 1 and a % 4 == 3:
            return True
        
    # 5. Check if a is a cube of 5
    if a % 5 == 0:
        if a % 5 == 0 and a % 5 == 1:
            return True
        elif a % 5 == 0 and a % 5 == 2:
            return True
        elif a % 5 == 0 and a % 5 == 3:
            return True
        elif a % 5 == 0 and a % 5 == 4:
            return True
        
    # 6. Check if a is a cube of 6
    if a % 6 == 0:
        if a % 6 == 0 and a % 6 == 1:
            return True
        elif a % 6 == 0 and a % 6 == 2:
            return True
       
