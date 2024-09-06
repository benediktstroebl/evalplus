
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    # 使用一个空列表来保存返回结果
    result = []
    
    # 使用一个字符串变量 i 来保存当前偏移量
    i = 0
    
    # 使用一个字符串变量 j 来保存当前结果长度
    j = 0
    
    # 使用一个字符串变量 s 来保存输入字符串
    s = s
    
    # 使用一个布尔变量 has\_vowel 来保存是否有数字
    has_vowel = False
    
    while i < len(s):
        # 如果字符为空格，继续往下偏移
        if s[i] == " ":
            i += 1
            continue
        
        # 如果字符为数字，结束循环，返回结果
        if s[i] in "0123456789":
            result.append(s[i])
            i += 1
            continue
        
        # 如果字符为字母，开始判断
        while True:
            if s[i] == " ":
                # 如果遇到了空格，判断结束
                break
            
            elif s[i] == "a" or s[i] == "b" or s[i] == "c" or s[i] == "d" or s[i] == "e" or s[i] == "f" or s[i] == "g" or s[i] == "h" or s[i] == "i" or s[i] == "j" or s[i] == "k" or s[i] == "l" or s[i] == "m" or s[i] == "n" or s[i] == "o" or s[i] == "p" or s[i] == "q" or s[i] == "r" or s[i] == "s" or s[i
