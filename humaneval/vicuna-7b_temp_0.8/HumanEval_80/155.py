
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
    # First, find the length of the string s
    n = len(s)
    
    # Then, iterate through the string and check if every 3 consecutive letters are distinct
    distinct_triplets = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if s[i:j] == s[j:k] == s[k:i]:
                    distinct_triplets = 0
                    break
                elif s[i:j] != s[j:k] != s[k:i]:
                    distinct_triplets += 1
                else:
                    distinct_triplets += 2
    
    return distinct_triplets >= 3