Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]

def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome that begins with the supplied string s """
    if not s:
        return s

    # find the location of the longest palindrome suffix
    j = len(s) - 1
    while j >= 0 and not is_palindrome(s[j:]):
        j -= 1

    if j == -1:
        return s

    # reverse the prefix up to the palindrome suffix, and append to s
    p = s[:j] + s[j:][::-1]
    return p + make_palindrome(p)
``` 

This script defines two functions:
- The `is_palindrome` function takes a string as input and checks whether it is a palindrome by comparing it to its reverse.
- The `make_palindrome` function takes a string as input and returns the shortest palindrome string that starts with the input string. 

In the `make_palindrome` function:
- If the input string is empty, it returns the empty string.
- Otherwise, it searches for the longest palindrome suffix in the input string.
- If no palindrome suffix is found, it returns the input string.
- Otherwise, it constructs the shortest palindrome by:
    - Taking the portion of the input string before the palindrome suffix.
    - Reversing this portion.
    - Appending the reversed portion to the input string.
    - Repeating this process by recursively calling `make_palindrome` on the combined string until a palindrome is reached.