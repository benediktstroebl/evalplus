```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string): 
    """ Find the shortest palindrome that begins with a supplied string """
    
    #Algorithm idea:
    # Find the longest postfix of supplied string that is a palindrome
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    
    if not string: 
        return ''

    # Find the longest palindrome 
    longest_palindrome = ""
    for char in string: 
        if char == char[::-1]: 
            longest_palindrome += char 
            continue
        else: 
            if longest_palindrome != "": 
                longest_palindrome += char 
            else: 
                return longest_palindrome 

    # Reverse the prefix and append the suffix 
    return longest_palindrome[::-1] + longest_palindrome
```