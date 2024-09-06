Here is a Python script with a self-contained function that solves the problem of finding the shortest palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    # Algorithm idea:
    # Find the longest postfix of supplied string that is a palindrome
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    
    # Convert string to lowercase to ensure palindrome
    string = string.lower()
    
    palindrome = []
    i = 0
    while i < len(string):
        is_palindrome = True
        j = i
        while j < len(string) and string[j] == string[j - 1]:
            j += 1
        if j == len(string):
            is_palindrome = False
        if is_palindrome:
            palindrome.append(string[j -
            j -= 1
        i = j + 1
    
    return ''.join(palindrome)
```
This Python code defines a function `make_palindrome` that constructs the shortest palindrome based on a given string. It uses a algorithm to find the longest palindromizable prefix within the string, and then appends its reverse to create the palindrome. The function also converts the string to lowercase to ensure correct palindrome formation. The solution can the example demonstrates the function's usage for different input strings.