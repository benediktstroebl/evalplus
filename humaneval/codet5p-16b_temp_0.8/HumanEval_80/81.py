
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

    if len(s) < 3:
        return False
    
    last_seen = {}
    while True:
        s = "".join(sorted(s))
        for i, c in enumerate(s):
            if c not in last_seen:
                last_seen[c] = [i]
            else:
                last_seen[c] += [i]
        
        new_s = ""
        for c in s:
            new_s += c
            if c in last_seen and len(last_seen[c]) == 2:
                del last_seen[c]
        s = new_s
        if not last_seen:
            break
    
    return len(s) >= 3
