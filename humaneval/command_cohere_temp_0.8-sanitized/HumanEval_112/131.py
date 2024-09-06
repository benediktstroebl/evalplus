def reverse_delete(s, c):
    s_set = set(s)
    c_set = set(c)
    # delete characters in s that are in c
    s = ''.join(x for x in s if x not in c_set)
    # check if the result is a palindrome
    return (s, s == s[::-1])