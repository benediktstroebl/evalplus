
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
    m,n=len(s),0
    for i in range(n+1):
        for j in range(i+1,min(m,n)+1):
            if s[j-i-1]==s[j-i-2] or s[j-i-1]==s[j-i-3] or s[j-i-1]==s[j-i-4]:
                return False
        if s[j-i-1]!='\0':
            n=i+1
    return True
