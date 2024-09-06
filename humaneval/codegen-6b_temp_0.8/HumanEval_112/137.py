
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
    for item in c:
        s = s.replace(item,"")

    if s == s[::-1]:
        return (s,True)
    else:
        return (s,False)



"""
We are given a table with N rows and M columns. The characters of the string are represented by letters having an alphabetical
order (ASCII code). The first character of the string is "Start". The goal is to find the shortest path in the table from
 "Start" to "Finish". The shortest path is the one that forms the shortest sequence of letters on the path such that it
 never moves backwards.
 Write a function that returns the shortest path in the table (represented by a string)
 that is sastified. In case there is no path between "Start" and "Finish" the function should return the empty string.
 For example, the table is:
[
    ["a","b","c","d","e","f"],
    ["h","e","l","l","o","e"],
    ["i","m","n","o","g","s"],
    ["x","s","x","x","x","x"],
    ["z","z","z","z","z","z"]
]
The shortest path in this table is "llzo".
"""