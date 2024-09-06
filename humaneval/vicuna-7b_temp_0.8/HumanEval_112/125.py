
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
    # We will use two pointers, one for the left side and one for the right side of the string
    # We will start by comparing the first character of the left and right side of the string
    # if they are equal, we will move the pointer to the right side and check the next character
    # if it is different, we will compare it with the next character of the right side
    # if they are equal, we will move the pointer to the left side and compare the next character
    # if it is different, we will return False
    # if the left and right side of the string are the same, we will return True
    # we will continue this process until we reach the end of the string
    # We will also store the characters that we have deleted in a list
    # at the end, we will return the result string and True/False for the check
    result = ''
    characters_to_delete = []
    for i in range(len(s)):
        if s[i] == c[0]:
            result += s[i]
            for j in range(len(c)):
                if c[j] == s[i+1]:
                    result += s[i+1]
                    characters_to_delete.append(s[i])
                    break
        else:
            if s[i] != c[j]:
                return False
            characters_to_delete.append(s[i])
    result += ''.join(characters_to_delete)
    return result, True
