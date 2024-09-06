```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''.join()
    else:
        palindrome = string[:-1]  # get the first non-palindrome part
        while True:
            suffix = palindrome + string[len(palindrome):]
            if is_palindrome(suffix):
                palindrome += suffix[::-1]  # append reverse of current suffix
                break
            else:
                palindrome += suffix
        return palindrome
```
The is_palindrome function checks if a given string is a palindrome or not. It returns a Palindrome is a sequence that reads the same way forward and backward, such as the "heart" of this sequence. The make_palindrome function finds the shortest palindrome that begins with a supplied string. It uses a algorithm idea to construct the palindrome. The function returns '''' if no palindrome is found.