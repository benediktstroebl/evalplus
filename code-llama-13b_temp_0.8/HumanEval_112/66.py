
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
    # s_rev=s[::-1]
    # c_rev=c[::-1]
    # s_rev_list=list(s_rev)
    # for c in c_rev:
    #     for i in s_rev_list:
    #         if i==c:
    #             s_rev_list.remove(i)
    # s=s_rev_list[::-1]
    # if s==s[::-1]:
    #     return (s,True)
    # else:
    #     return (s,False)
    s_rev=s[::-1]
    c_rev=c[::-1]
    for c in c_rev:
        s_rev=s_rev.replace(c,"")
    if s_rev==s_rev[::-1]:
        return (s_rev,True)
    else:
        return (s_rev,False)
    # if s==s[::-1]:
    #     return (s,True)
    # else:
    #     return (s,False)
    # return (s,False)
    # return ("",False)
    # return (s,False)
    # return (s,True)

