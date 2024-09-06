
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
    s_list=s.split()
    c_list=c.split()
    for i in range(len(c_list)):
        if s_list[0]==c_list[i]:
            for j in range(1,len(s_list)):
                if s_list[j]==c_list[i]:
                    s_list.remove(s_list[j])
                else:
                    break
    if s_list==[]:
        return ''.join(c_list),True
    else:
        return ''.join(s_list),False
