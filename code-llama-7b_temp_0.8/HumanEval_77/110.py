
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
    #---------------------------
    # YOUR CODE STARTS HERE
    
    a = abs(a)
    return (a == a**(1/3))
    
    #---------------------------
    # YOUR CODE ENDS HERE

    #---------------------------
    # TEST CODE STARTS HERE
    
    test = iscube(1)
    if test:
        print("Pass")
    else:
        print("Fail")

    test = iscube(2)
    if test:
        print("Fail")
    else:
        print("Pass")

    test = iscube(-1)
    if test:
        print("Pass")
    else:
        print("Fail")

    test = iscube(64)
    if test:
        print("Pass")
    else:
        print("Fail")

    test = iscube(0)
    if test:
        print("Pass")
    else:
        print("Fail")

    test = iscube(180)
    if test:
        print("Fail")
    else:
        print("Pass")


    #---------------------------
    # TEST CODE ENDS HERE

