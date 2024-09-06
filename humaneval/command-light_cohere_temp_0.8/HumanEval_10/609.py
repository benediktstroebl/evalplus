```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    # Find the longest postfix of supplied string that is a palindrome
    longest_palindrome = [0]
    for i in range(1, len(string)):
        if is_palindrome(string[i:]):
            longest_palindrome = longest_palindrome[::-1] + string[i:]
        else:
            break

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return longest_palindrome + string[-longest_palindrome:]
```
The function `is_palindrome` checks if a given string is a palindrome, and the function `make_palindrome` uses this function to create a palindrome.