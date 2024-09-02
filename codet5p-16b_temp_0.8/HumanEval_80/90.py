
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

    s_list = list(s)
    for i in range(3, len(s_list) + 1): #len(s_list) + 1 because len() does not include last element
        for j in range(0, len(s_list) - i + 1):
            if not s_list[j:j+i] in s_list[j+1:j+i]:
                return False
    return True
    
    
    
