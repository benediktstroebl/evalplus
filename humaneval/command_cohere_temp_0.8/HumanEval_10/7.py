Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(s: str) -> bool:
    """ Returns true if string s is a palindrome, false otherwise """
    return s == s[::-1]

def make_palindrome(s: str) -> str:
    """ Returns the shortest palindrome string that starts with s """
    if not s:
        return s

    # find the position of the longest palindrome suffix
    palindrome_suffix_pos = len(s) - len(s)[::-1].find(s)

    # extract the palindrome suffix
    palindrome_suffix = s[-(palindrome_suffix_pos):]

    # walk backwards up to the palindrome suffix to find the shortest matching prefix
    prefix = s[:-(s[::-1].rfind(palindrome_suffix[:-1]))]
    
    # construct the return string by concatanating prefix and reverse of suffix
    return f"{prefix}{palindrome_suffix[::-1]}"

# tests
assert is_palindrome("racecar")
assert not is_palindrome("hello")

assert make_palindrome("a") == "a"
assert make_palindrome("cat") == "catac"
assert make_palindrome("catas") == "catac"
``` 

The `make_palindrome` function works by:
1. Checking if the supplied string is empty. If so, it returns the string.
2. Finding the longest palindrome suffix of the supplied string. This is done by finding the length of the reverse of the suffix which matches the original string. This length is the position of the palindrome suffix.
3. Extracting the palindrome suffix.
4. Finding the shortest matching prefix by walking backwards in the string up to the palindrome suffix. This is done by reversing the palindrome suffix (excluding the last character) and finding its index in the reversed string.
5. Using the extracted prefix and reverse the palindrome suffix to return the shortest palindrome.