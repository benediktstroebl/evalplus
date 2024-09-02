
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
    """Response
    # create a result string, without the characters in c
    result = ""
    # for each character in s, check if it is not in c, if so, add it to the result
    for char in s:
        if char not in c:
            result += char
    # check if the result is a palindrome
    # a palindrome is a string that reads the same backward as forward, so check if result is equal to result reversed
    if result == result[::-1]:
        return result, True
    else:
        return result, False
    """
    """Refactor 1
    # using comprehension
    # create a result string, without the characters in c
    result = "".join([char for char in s if char not in c])
    # check if the result is a palindrome
    # a palindrome is a string that reads the same backward as forward, so check if result is equal to result reversed
    if result == result[::-1]:
        return result, True
    else:
        return result, False
    """
    """Refactor 2
    # using list comprehension
    # create a result string, without the characters in c
    result = "".join([char for char in s if char not in c])
    # check if the result is a palindrome
    # a palindrome is a string that reads the same backward as forward, so check if result is equal to result reversed
    if result == result[::-1]:
        return result, True
    else:
        return result, False
    """
    """Refactor 3
    # using filter
    # create a result string, without the characters in c
    result = "".join(filter(lambda char: char not in c, s))
    # check if the result is a palindrome
    # a palindrome is a string that reads the same backward as forward, so check if result is equal to result reversed
    if result == result[::-1]:
        return result, True
    else:
        return result, False
    """
    """Refactor 4
    # using map
    # create a result string, without the characters in c
