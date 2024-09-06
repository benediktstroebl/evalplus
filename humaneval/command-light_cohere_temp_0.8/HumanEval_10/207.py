Here's the solution:
```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    # Finds the shortest palindrome that begins with a supplied string
    palindrome = ""
    for char in string:
        if palindrome and char == palindrome[-1] :
            palindrome += char[::-1]
        else:
            palindrome = char
```

The `is_palindrome` function checks if a given string is a palindrome or not, by comparing the string with its reverse. The `make_palindrome` function finds the shortest palindrome that begins with a supplied string. It iterates through string's characters and checks if the character is equal to the reverse of the last character in the `palindrome` string.  The process continues until it finds the palindrome.