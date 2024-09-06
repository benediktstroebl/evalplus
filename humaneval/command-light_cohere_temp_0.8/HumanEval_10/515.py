```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindromic_prefix = next((sub for sub in string if is_palindrome(sub)),
                    len(string) - len(palindromic_prefix) - 1)
    return palindromic_prefix + string[len(palindromic_prefix):]
```
The code defines two functions: `is_palindrome` checks if a given string is a palindrome and returns a boolean value, and `make_palindrome` returns a new string that is the shortest palindrome that begins with the given string. The `make_palindrome` function uses a recursive algorithm to find the longest palindromic prefix in the string and then appends the reverse of that prefix to the end of the string to create the palindrome.