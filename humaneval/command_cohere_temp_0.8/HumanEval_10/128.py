Here's a Python script with a self-contained function that solves the problem using Python regex:
```python
import re

def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome """
    return s == s[::-1]

def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    palindrome = s + ''.join(re.findall(f'(.*)({s}[a-zA-Z]*){s}', s + s[::-1]))
    return palindrome
```

This code uses the re module to utilize regex to find the longest palindromic suffix and reverses and prepends it to the front to create new candidates until no more palindromes can be generated. It considers all possible substrings of the original string and their reverses to find the shortest palindrome.

Note: The regex could be made non-case sensitive by including the i flag in the search, like this: `re.findall(f'(.*)({s}[^a-zA-Z]*){s}', s + s[::-1])`. However, case sensitivity depends on problem statement.