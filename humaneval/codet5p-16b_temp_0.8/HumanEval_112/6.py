
def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """

    s_dic = dict()
    c_dic = dict()
    for i in range(len(s)):
        if s[i] in c_dic:
            c_dic[s[i]] += 1
        else:
            c_dic[s[i]] = 1
        if s[i] in s_dic:
            s_dic[s[i]] += 1
        else:
            s_dic[s[i]] = 1

    if c_dic == s_dic:
        return (s,False)
    elif c_dic!= s_dic:
        c_list = list(c_dic.keys())
        s_list = list(s_dic.keys())
        for i in range(len(s_list)):
            if c_list[0]!= s_list[0]:
                c_dic[s_list[0]] -= 1
                s_dic[s_list[0]] -= 1
                c_list.pop(0)
                s_list.
