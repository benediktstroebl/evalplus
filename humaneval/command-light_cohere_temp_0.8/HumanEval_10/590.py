Here is a Python script with a self-contained function that solves the problem of finding the shortest palindrome:
```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    # Function to make a palindrome
    # Idea: 
    # Find the longest postfix of supplied string that is a palindrome
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    
    # initialise empty string 
    result = ''
    
    # find the longest palindrome 
    longest_palindrome = ''
    
    for char in string:
        # if char is a palindrome
        if is_palindrome(char):
            # append the char
            longest_palindrome = char
        else:
            # append the longest_palindrome
            longest_palindrome = longest_palindrome[-1:] + char
            
    # reverse the longest_palindrome 
    result = longest_palindrome[-1:] + longest_palindrome
    
    return result
```
The function is_palindrome checks if a given string is a palindrome, and the make_palindrome function creates a palindrome from a given string by finding the longest palindrome of the characters.