
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
    d = {}
    for x in s:
        if x in d:
            d[x]+=1
        else:
            d[x]=1


    for x in c:
        if x in d:
            d[x]-=1
            if d[x]<0:
                return '',False
    flag = True
    s=''
    for x in s:
        if d[x]>0:
            s+=x
        else:
            flag=False
            break

    return s,flag

assert reverse_delete('abcdedcba','b')==('cdedc',True)
assert reverse_delete('abcdedcba','ab')==('cdedc',False)
assert reverse_delete('abcdedcba','bd')==('cd',False)
