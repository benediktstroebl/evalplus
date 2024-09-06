
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
    # fill in the following function
    ans = ''
    i,j = 0,len(s)-1
    while i < j:
        while i < j and s[i] != c[i]:
            ans += s[i]
            i += 1
        while i < j and s[j] != c[j]:
            ans += s[j]
            j -= 1
        if i < j:
            ans += s[i]
            i += 1
            ans += s[j]
            j -= 1
    return (ans,ans==s[::-1])

assert reverse_delete('ade', 'de') == ('', False)
assert reverse_delete('abcde', 'a') == ('bcde', False)
assert reverse_delete('abcdedcba', 'b') == ('cdedcba', True)
assert reverse_delete('abcdedcba', 'b') == ('cdedcba', True)
assert reverse_delete('abcd', 'b') == ('abcd', False)

assert reverse_delete('gosh', 'osh') == ('goosh', True)
assert reverse_delete('gosh', 'osh') == ('goosh', True)
assert reverse_delete('gosh', 'osh') == ('goosh', True)
assert reverse_delete('car', 'rac') == ('carrac', True)
assert reverse_delete('car', 'rac') == ('carrac', True)
assert reverse_delete('car', 'rac') == ('carrac', True)
assert reverse_delete('carel', 'racel') == ('carab', True)
assert reverse_delete('carel', 'racel') == ('carab', True)
assert reverse_delete('carel', 'racel') == ('carab', True)
assert reverse_delete('carl', 'racel') == ('carale', True)
assert reverse_delete('carl', 'racel') == ('carale', True)
assert reverse_delete('carl', 'racel') == ('carale', True)
assert reverse_delete('now', 'wawn') == ('wnowl', True)
assert reverse_delete('now', 'wawn') == ('wnowl', True)
assert reverse_