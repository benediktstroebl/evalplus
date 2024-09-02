
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    
    #Create a set
    hSet = set()

    #Loop through the string
    for i in range(0, len(s)):
        #Add the current letter to the set
        if s[i] in hSet:
            return False
        else:
            hSet.add(s[i])

    #If the length of the set is less than 2 then return False
    if len(hSet) < 2:
        return False
    else:
        return True
    
