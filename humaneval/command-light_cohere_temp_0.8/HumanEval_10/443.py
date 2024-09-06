```python
def is_palindrome(string): 
    """ Check if a given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string): 
    """ Create a palindrome from a non-palindrome string """
    
    # Algorithm idea: 
    # - Find the longest postfix of supplied string that is a palindrome
    # - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    
    # Check if empty string
    if string == "":
        return ""

    # Check if only characters are palindromes
    # (E.g., c, g, a, t, d)
    # and there are enough characters, 
    # then return the entire string as palindrome
    if string == string[::-1]:
        return string
    
    # Check for other strings with non-palindrome characters
    # and create a palindrome using string prefix and postfix
    postfix = ''
    prefix = string[:0:-1]
    
    # Find the index of last non-palindrome character
    # in the string and prefix
    i = len(string) - 2
    j = len(prefix) - 1
    while i >= 0 and j >= 0:
        if string[i] != prefix[j]:
            break
        i -= 1
        j -= 1
        
    if i == -1 and j == -1:
        return prefix + postfix
    
    # Find the index of the first palindrome character
    # in the string and prefix
    k = 0
    while k < i and string[k] == prefix[j]:
        k += 1
        j -= 1
        
    postfix = prefix[j+1:k+1] + postfix
    return prefix + postfix
```