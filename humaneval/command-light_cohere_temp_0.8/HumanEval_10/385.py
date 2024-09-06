Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1] 

def make_palindrome(string): 
    """ Find the shortest palindrome that begins with a supplied string """
    
    #Check if the string is empty
    if not string:
        return string
    
    #Find the longest palindrome of the first half
    result = []
    for i, char in enumerate(string[: len(string) // 2]):
        if is_palindrome(char):
            result.append(char)
            continue
    #Find the longest palindrome of the second half
    result.append(string[i + len(string) // 2])
    
    #Reverse the whole string 
    return ''.join(''.join(reversed(result))
```
The function is_palindrome checks if the given string is a palindrome. The make_palindrome function then finds the shortest palindrome that begins with the supplied string by iterating through the string and checking if each character is a palindrome.