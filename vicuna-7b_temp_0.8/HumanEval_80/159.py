
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
    seen = set()
    count = Counter()
    for char in s:
        if char.isalpha() and char not in seen:
            seen.add(char)
            count[char] += 1
    return count <= len(s) // 3 and all(all(sorted(chars, key=ord) for chars in count.most_common(len(s) // 3)) for _ in range(len(s)))