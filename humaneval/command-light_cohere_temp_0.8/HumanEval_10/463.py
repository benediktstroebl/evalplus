Here's the solution to the Markdown code block problem:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""
    # find the longest palindrome substring
    max_palindrome = ""
    for char in string:
        if is_palindrome(char):
            max_palindrome = max(max_palindrome[:-palindrome]+char)
    # reverse the prefix and append the longest palindrome
    return max_palindrome[::-1] + max_palindrome[-1:]
```
This function is a self-contained Python function that uses string slicing to check if a string is a palindrome and then constructs a palindrome using the longest palindrome substring.