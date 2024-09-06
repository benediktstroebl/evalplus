
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
    for i in s:
        if i in c:
            s=s.replace(i,"",1)
    if s==s[::-1]:
        return (s,True)
    else:
        return (s,False)

assert reverse_delete("bbb","bb") == ("bbbb",True)
assert reverse_delete("bbb","bbb") == ("bbb",True)
assert reverse_delete("a","a") == ("a",True)
assert reverse_delete("a","aa") == ("aa",False)
assert reverse_delete("abcdedcba","b") == ("abcdedcba",True)
assert reverse_delete("abcdedcba","ab") == ("abcdedcba",True)
assert reverse_delete("abcdedcba","ba") == ("abcded",False)
assert reverse_delete("abcdedcba","abc") == ("dedcba",False)
assert reverse_delete("abcdedcba","ded") == ("cba","False")
assert reverse_delete("abcdedcba","cba") == ("dedc","False")
assert reverse_delete("abcdedcba","abcded") == ("dedc","False")
assert reverse_delete("abcdedcba","dedc") == ("c","False")
assert reverse_delete("abcdedcba","c") == ("","False")
assert reverse_delete("abcdedcba","bc") == ("","False")
assert reverse_delete("abcdedcba","abcdedc") == ("","False")
assert reverse_delete("abcdedcba","dedcbed") == ("dedc","False")
assert reverse_delete("abcdedcba","bd") == ("de","False")
assert reverse_delete("abcdedcba","de") == ("cba","False")
assert reverse_delete("abcdedcba","cba") == ("","False")
assert reverse_delete("abcdedcba","dedc") == ("","False")
assert reverse_delete("abcdedcba","abcdedc") == ("","False")
assert reverse_delete("abcdedcba","dedcbed") == ("dedc","False")
assert reverse_delete("abcdedcba","dedcbed") == ("","False")
