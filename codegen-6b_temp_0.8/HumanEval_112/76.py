
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
    new_s = ''
    is_palindrome = True
    for i in s:
        if i not in c:
            new_s += i
    if new_s == new_s[::-1]:
        is_palindrome = True
    else:
        is_palindrome = False

    return (new_s, is_palindrome)
assert reverse_delete("abcde", "ae") == ('bcd', False)
assert reverse_delete("abcdedcba","ab") == ('cdedc',True)
assert reverse_delete("abcde", "b") == ('cde', False)
assert reverse_delete('abccba', 'abcd') == ('bc', True)
assert reverse_delete("abcdedcba", "b") == ('cdedc', True)
assert reverse_delete("adbccba", "abcd") == ('d', True)
assert reverse_delete("adbccba", "abcd") == ('d', True)

