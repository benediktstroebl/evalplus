```python
def reverse_delete(s, c):
    s_set = set(s)
    c_set = set(c)
    # delete characters in s that are in c
    s = ''.join(char for char in s if char not in c_set)
    # check if the result string is a palindrome
    return (s, s == s[::-1])
```
The code uses sets to delete characters in s that are in c, and then checks if the remaining string is a palindrome. You can test this code on your own to see if it passes the test suite. 
To better understand this solution let's break it down step-by-step:
- The sets s_set and c_set are created using the provided strings s and c to allow for efficient membership testing.
- The string s is then reconstructed using string concatenation to avoid deleting any characters in s that are in c.
- The result string is then compared to its reverse ('s[::-1]') to determine if it's a palindrome. The True or False value is returned as part of a tuple with the edited string s. 

Overall, this is a clear and concise solution to the problem that uses sets and string manipulation to achieve the desired result.