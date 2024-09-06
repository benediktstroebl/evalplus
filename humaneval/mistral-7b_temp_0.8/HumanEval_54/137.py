

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    # your code here
    # 一次遍历
    # 将字符统计到字典中
    # 判断另一个字符串字典中是否存在
    # 存在字典中则说明是同一个字符
    s0_dict = {}
    for ch in s0:
        s0_dict[ch] = s0_dict.get(ch, 0) + 1
    for ch in s1:
        if ch in s0_dict:
            s0_dict[ch] -= 1
        else:
            return False
    return True

