```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string
    Algorithm idea: 
    - Find the longest postfix of supplied string that is a palindrome. 
    - Append to theend of the string reverse of a string prefix that comes before the palindromic suffix. 
    Return with empty string as first prefix and empty string as last suffix """
    
    # First empty string is a palindrome
    prefix = ''
    suffix = ''
    
    while True:
        # Find the longest palindrome among prefix, string[0:index], and suffix
        max_palindrome = min(len(prefix + string[0:index]) + len(string[index:]), 
                           len(prefix + string[:index]) + len(string[index:]) ,
                           len(prefix) + len(string[0:index]) + len(suffix))
        
        # Append the longest palindrome as the next character
        if max_palindrome > 0:
            prefix += str(index)
            suffix += str(index)
            index += 1
        
        # Reverse the prefix and suffix to make a palindrome
        prefix = prefix[::-1]
        suffix = suffix[::-1]
    
    return prefix + suffix
```