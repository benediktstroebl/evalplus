
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
    # Write your code here
    lst=[]
    for i in range(len(s)):
        lst.append(s[i:i+3])
    a=set(lst)
    if len(a)==1:
        return True
    else:
        return False
    # time complexity: O(N^2)
    # space complexity: O(N)

