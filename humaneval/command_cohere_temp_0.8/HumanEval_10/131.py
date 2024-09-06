Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]

def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    if not s:
        return s

    # find longest palindrome suffix
    i = len(s) - 1
    while i > 0 and not is_palindrome(s[i:]):
        i -= 1

    # find corresponding palindrome prefix
    j = 0
    while not is_palindrome(s[:j] + s[i:i][::-1] ):
        j += 1

    return s[:j] + s[i:i][::-1]
``` 

Note, the make_palindrome() function assumes that a palindrome can only consist of a single character, hence the [::-1] indexing trick, and any string of length 1 is a palindrome.