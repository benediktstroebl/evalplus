
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
    #fruit = 'apple'
    #letter = 'a'

    result = []
    result = list(s)
    #print(result)
    #print(result.count('a'))
    if result.count(c) > 0:
        for i in range(0, len(result)):
            if result[i] == c:
                result.pop(i)
                i-=1
    #print(result)
    result = ''.join(result)
    result = result[::-1]
    print(result)
    print(c)
    print(result.count(c))
    if result == c:
        print('True')
    else:
        print('False')

