
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
    # c_list = list(c)
    # result = [ch for ch in s if ch not in c_list]
    # result_str = ''.join(result)
    # print(result)
    # print(result_str)
    # if result_str[::-1] == result_str:
    #     return (result_str,True)
    # else:
    #     return (result_str,False)
    # 字符串切片方法
    c_list = list(c)
    result_list = [ch for ch in s if ch not in c_list]
    result_str = ''.join(result_list)
    # 截取开始到结束位置的字符串，左闭右开，左开右闭
    if result_str[::-1] == result_str[:len(result_str)]:
        return (result_str,True)
    else:
        return (result_str,False)
