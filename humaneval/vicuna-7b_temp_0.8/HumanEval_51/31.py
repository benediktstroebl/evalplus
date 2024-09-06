

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    # 判断字符串是否为空
    if text == '':
        return ''
    # 判断字符串是否为单词
    if len(text) <= 2:
        return text
    vowels = 'aeiouAEIOU'
    # 遍历字符串
    for char in text:
        # 如果字符串中的每个字符不是词汇，忽略
        if not char.isalpha():
            continue
        # 如果字符串中的每个字符不是词汇，忽略
        if not char.isalpha():
            continue
        # 如果字符串中的每个字符不是词汇，忽略
        if not char.isalpha():
            continue
        # 判断字符串中的每个字符是否在词汇中
        if any(c.lower() in vowels.lower() for c in char):
            # 如果字符串中的每个字符是词汇的，则替换为空字符串
            return ''
    # 如果字符串中的每个字符不是词汇，则返回字符串本身
    return text
