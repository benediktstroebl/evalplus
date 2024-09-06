```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string): 
    """ Find the shortest palindrome that begins with a supplied string.
    if not string: return ''
    palindrome = []
    for char in string: 
        if char == char[::-1]: 
            palindrome.append(char) 
        else: 
            palindrome.append(char[::-1])  
    return ''.join(palindrome)
```
The code defines two functions, is_palindrome and make_palindrome, that tests and creates a palindrome for a given string. 

The is_palindrome function checks if a given string is a palindrome by comparing it with its reverse. The make_palindrome function creates a palindrome for a given string by first checking if the string is empty. If it's not, it initializes a list of characters in the string, then checks each character in the string to see if it is the same as its reverse. If it is true, it adds the character to the list.