

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return sorted(s0) == sorted(s1)

"""
In a weighted alphabet (let's call it A), a character c is said to belong to a class of weight w if
it is more likely than any other character to belong to that class.

We define that a string s is in the class of weight w if the frequency of character c in s is at least as
high as the frequency of character c in the string made only from characters that belong to the class of
weight w.

For example, the string "abbccc" is a class of weight 1, because the frequency of 'a' is 3, while the
frequency of 'b' is 2, while the frequency of 'c' is 4, and the frequency of 'd' is 1.

The string "aabbccdd" is a class of weight 2, because 'a' is more likely than 'b', 'b' more likely than
'c', and 'c' more likely than 'd'.

Write a function count_classes(s: str, w: int) -> int that counts the number of classes of weight w
that s consists of.

For example, if s = "abbccc", then your function would return 3, because the string "abbccc" is a class
of weight 3 that contains characters 'a', 'b', and 'c', and two more classes of weight 2 that contain
characters 'd' and 'e'.

If s = "aabbccdd", then your function would return 4, because the string 'aabbccdd' is a class of
weight 4 that contains characters 'a', 'b', 'c', 'd', and 'e'.

Hint: Use a hashtable to store the frequencies of all characters in s and then use Python's builtin
count() function.

For example, the following code counts the number of classes of weight 1 that are present in the string
"abbccc":
