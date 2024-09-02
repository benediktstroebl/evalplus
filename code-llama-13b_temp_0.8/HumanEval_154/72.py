
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # Checking if the second word is a substring of the first word
    if b in a:
        return True
    # else check if any of its rotations is a substring in the first word
    # Method 1: Creating a substring of all the rotations of b
    # String slicing
    # Slicing b
    # 1st rotation
    b_rot1 = b[1:] + b[0]
    # 2nd rotation
    b_rot2 = b[2:] + b[0:2]
    # 3rd rotation
    b_rot3 = b[3:] + b[0:3]
    # 4th rotation
    b_rot4 = b[4:] + b[0:4]
    # 5th rotation
    b_rot5 = b[5:] + b[0:5]
    # 6th rotation
    b_rot6 = b[6:] + b[0:6]
    # Creating the concatenated string of all the rotations of b
    b_rot_conc = b_rot1 + b_rot2 + b_rot3 + b_rot4 + b_rot5 + b_rot6
    # Checking if any of the rotations of b is a substring of a
    if b_rot1 in a:
        return True
    if b_rot2 in a:
        return True
    if b_rot3 in a:
        return True
    if b_rot4 in a:
        return True
    if b_rot5 in a:
        return True
    if b_rot6 in a:
        return True
    return False
    
    # Method 2: Iterating over the rotations of b and checking if it is a substring of a
    # for i in range(len(b)):
    #     if b[i:] + b[:i] in a:
    #         return True
    # return False

