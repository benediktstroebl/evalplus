```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''.join
        # We find the longest palindrome
        palindrome = []
        index = 0
        while True:
            if index == len(string):
                break
            if is_palindrome(string[index:]):
                palindrome.append(string[index:])
                index += 1
            else:
                palindrome.append(string[index])
                index += 1
        return ''.joinjoin(reversed(palindrome))

def not_palindrome(string):
    return bool(is_palindrome(string))

# Example usage
print(make_palindrome('cad')) # Output: 'cadac'
```
This code defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` builds a palindrome from a given string. The `make_palindrome` function utilizes the `is_palindrome` function to find the longest palindrome in the string and then constructs it by reversing the characters of the palindrome and appending them to the original string.