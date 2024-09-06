
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
    # create an empty list to store the results
    result = []

    # iterate through the string
    for i in range(0, len(s)-2):
        # check if the 3 consecutive letters are distinct
        if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
            result.append(s[i:i+3])

    # check if all the 3-letter substrings are unique
    if len(set(result)) == len(result):
        return True
    else:
        return False
