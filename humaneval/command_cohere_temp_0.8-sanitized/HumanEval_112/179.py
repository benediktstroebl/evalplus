def reverse_delete(s, c):
    s_set = set(s)
    c_set = set(c)
    # remove characters in s that are in c
    s = ''.join(char for char in s if char not in c_set)
    # check if s is a palindrome
    return s, s == s[::-1]