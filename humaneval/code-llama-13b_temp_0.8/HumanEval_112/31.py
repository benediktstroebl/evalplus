
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
    # def is_palindrome(string):
    #     left, right = 0, len(string) - 1
    #     while left < right:
    #         if string[left] != string[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True
    def is_palindrome(s):
        return s == s[::-1]
    new_s = "".join(letter for letter in s if letter not in c)
    return (new_s, is_palindrome(new_s))

