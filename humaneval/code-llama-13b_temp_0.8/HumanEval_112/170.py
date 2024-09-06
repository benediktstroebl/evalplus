
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
    # hash_table = {}
    # for char in s:
    #     if char in hash_table:
    #         hash_table[char] += 1
    #     else:
    #         hash_table[char] = 1
    # print(hash_table)
    # for char in c:
    #     if char in hash_table:
    #         hash_table[char] -= 1
    # print(hash_table)
    # flag = True
    # for key in hash_table:
    #     if hash_table[key] != 0:
    #         flag = False
    # if flag:
    #     return (s,"")
    # else:
    #     result = ""
    #     for char in s:
    #         if char in hash_table and hash_table[char] == 0:
    #             continue
    #         else:
    #             result += char
    #     return (result,result[::-1]==result)
    
    # result = ""
    # for char in s:
    #     if char in c:
    #         continue
    #     else:
    #         result += char
    # return result[::-1]==result,result
    
    # result = ""
    # for char in s:
    #     if char in c:
    #         continue
    #     else:
    #         result += char
    # return result[::-1]==result,result
    
    # return (s.translate(s.maketrans("","",c)),s.translate(s.maketrans("","",c)) == s[::-1])
    # return (s.translate(s.maketrans(c,s[:0])),s.translate(s.maketrans(c,s[:0])) == s[::-1])
    return (s.translate(s.maketrans(c,s[:0])),s.translate(s.maketrans(c,s[:0])) == s[::-1])
    
    
