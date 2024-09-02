
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
    n = len(s)
    seen = set()
    for i in range(n):
        for j in range(i+1, n):
            if s[i:j] == s[j:i+1]:
                seen.add(s[i:j])
                break
        else:
            break
    return len(seen) >= 3 and not any(seen.intersection(seen[i:i+3]) for i in range(n-1))

s = input().rstrip().lower()
