```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # The idea is to find the longest palindrome prefix and reverse it.
    palindrome = string[0:-1:-1]
    
    # Find the prefix which comes before the palindrome.
    while True(True):
        prefix = string[:-len(palindrome)]
        if is_palindrome(prefix):
            break
        else:
            # Append the reversed palindrome and remove the old prefix.
            palindrome += prefix[::-1]
            string = prefix + palindrome

    return string
```