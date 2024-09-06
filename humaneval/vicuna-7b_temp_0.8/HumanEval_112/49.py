
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
    result = ""
    for i in s:
        if i not in c:
            result += i
    return result, True

if __name__ == "__main__":
    f = open("test.txt", "r")
    testcases = f.readlines()
    f.close()
    for testcase in testcases:
        print(testcase)
        s = testcase.strip()
        c = testcase.strip()
        result,is_palindrome = delete(s,c)
        print("Result:",result)
        print("Is Palindrome:",is_palindrome)