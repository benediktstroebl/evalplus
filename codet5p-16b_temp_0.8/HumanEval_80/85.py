
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
    hash_map = {}
    for letter in s:
        if letter in hash_map:
            hash_map[letter] += 1
        else:
            hash_map[letter] = 1
    seen = set()
    while True:
        if len(hash_map) == 1:
            return True
        hash_map_copy = hash_map.copy()
        for letter in hash_map:
            if hash_map[letter] == 1:
                if letter in seen:
                    return False
                seen.add(letter)
                for other_letter in hash_map_copy:
                    if hash_map[letter] == 1:
                        hash_map[other_letter] -= 1
                        if hash_map[other_letter] == 1:
                            return False
        break
    return False
