import unittest
def reverse_delete(s, c):
    s = [x for x in s if x not in c]
    s = ''.join(s)
    return s, s == s[::-1]