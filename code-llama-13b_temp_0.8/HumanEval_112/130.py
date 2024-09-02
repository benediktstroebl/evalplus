
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
    # dict that holds all chars
    chars_to_remove = {}

    # for each letter in c, store the occurences
    for letter in c:
        chars_to_remove[letter] = chars_to_remove.get(letter,0) + 1

    # store the letters we have to remove
    letters_to_remove = []

    # for each letter in s, if it is in chars_to_remove,
    # store it in letters_to_remove
    for letter in s:
        if letter in chars_to_remove:
            letters_to_remove.append(letter)

    # remove all letters in letters_to_remove from s
    for letter in letters_to_remove:
        s = s.replace(letter,'')

    # check if s is a palindrome, and return the result
    return s, s == s[::-1]
