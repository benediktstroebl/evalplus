
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

    def reversed_string(s,c):
        # initialize result
        result = ""
        # for each character in s
        for char in s:
            # if char not in c
            if char not in c:
                # append char to result
                result += char
        # return reversed result
        return result[::-1]

    def is_palindrome(s):
        # initialize left,right
        left, right = 0, len(s)-1
        # while left < right
        while left < right:
            # if s[left] != s[right]
            if s[left] != s[right]:
                # return False
                return False
            # increment left and right
            left += 1
            right -= 1
        # return True
        return True

    # initialize result
    result = reversed_string(s,c)
    # return (result,is_palindrome(result))
    return (result,is_palindrome(result))
