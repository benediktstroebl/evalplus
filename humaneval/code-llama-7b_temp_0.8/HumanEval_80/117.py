
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
    #first check length of string is at least 3, if not return False
    if len(s)<3:
        return False
    
    #create empty array with unique elements
    s_array = []

    #for loop to iterate through string and append to array
    for i in range(0,len(s)):
        s_array.append(s[i])
    
    #check if length is three or greater and elements are all unique
    if len(s_array)>=3 and len(set(s_array))==len(s_array):
        return True
    else:
        return False
    
