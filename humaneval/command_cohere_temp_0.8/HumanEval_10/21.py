Here's a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string
    
    # Find the longest palindromic suffix
    i = string.rfind('.{}'.format(string[::-1]))
    if i == -1:
        return string
    
    return string[:i] + string[i:i][::-1] + string[i+1:]
```

This code uses `.find()` and `[-1]` to reverse a string. The `find()` returns the first index where the substring is found. The `string.find('ee')` will return the index of the first occurrence of the substring 'ee'. The `string.find('.{}' '.format(string[::-1]))` will return the index of the substring started from the last character of the string and match until the reversed match is found. The `string[::-1]` reverses the string. After the longest palindromic suffix is found, the code slices the string to keep the palindrome and removes the rest. 

The idea to find the shortest palindrome is to grow the string incrementally by adding reverses of prefixes to a palindromic suffix. The code above works because it starts with the supplied string, which is guaranteed to have a palindromic suffix, and then works backward from the suffix to reverse and add prefixes until no more prefixes can be added.