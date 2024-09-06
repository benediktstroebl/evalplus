```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return 'error: unable to make palindrome'

    l = len(string)

    # find the longest palindrome prefix
    palindrome = string[:l // 2]

    while True:
        # find the suffix that is a palindrome
        suffix = string[-l // 2:]

        if suffix == palindrome:
            # append the reversed palindrome prefix and the suffix
            new_str = palindrome + suffix
            return new_str

        # move the search one position left
        l = l // 2

    return 'error: unable to make palindrome'
```
This script defines two functions: is_palindrome and make_palindrome. The is_palindrome function checks if a given string is a palindrome. The make_palindrome function attempts to make a palindrome of the string. It returns an error message string if the string cannot be made into a palindrome.