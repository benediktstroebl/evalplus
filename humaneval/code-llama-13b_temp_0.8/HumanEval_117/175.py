
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
    # your code here
    # 如果s为空，返回空列表
    if s == "":
        return []
    # 定义字典，统计出现字母次数
    dict = {}
    for i in s:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    # 定义列表，统计出现n次的字母
    lst = []
    for i in dict:
        if dict[i] == n:
            lst.append(i)
    # 定义列表，保存符合条件的词
    word_list = []
    # 使用三个变量，分别表示切片的开始位置、结束位置、当前位置
    start = 0
    end = 0
    current = 0
    # 遍历整个字符串
    for i in range(len(s)):
        # 如果当前字母是所需字符，那么开始、结束、当前位置都后移一位
        if s[i] in lst:
            start += 1
            end += 1
            current += 1
        # 如果当前字母不是所需字符，那么当前位置后移一位
        else:
            current += 1
        # 如果当前位置等于结束位置，则证明当前子串已经符合要求
        if current == end:
            # 定义一个临时变量temp，用于保存当前词
            temp = ""
            # 遍历当前词的所有字符
            for i in range(start, end):
                if s[i] != " ":
                    temp += s[i]
            # 将当前词添加到最终的词列表中
            if temp != "":
                word_list.append(temp)
            # 
