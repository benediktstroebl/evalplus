
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

    if len(s)==0:
        return s,True
    if s=='':
        return '',False
    if len(c)==0:
        return s,True
    c_set=set(c)
    s_set=set(s)
    if len(c_set.intersection(s_set))==0:
        return s,True
    
    c_set=c_set.intersection(s_set)
    s_set=s_set.difference(c_set)
    s_list=list(s)
    for i in s_set:
        index=s_list.index(i)
        s_list=s_list[:index]+s_list[index+1:]
    s=''.join(s_list)
    s=s.strip()
    return s,False

