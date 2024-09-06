Here is a Python script with a self-contained function that solves the problem of finding the shortest palindrome that begins with a supplied string:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""

    palindrome = []
    while True:
        palindrome.append(char)
        if is_palindrome(char):
            break
        else:
            reverse_char = char[::-1]
            palindrome.append(reverse_char)

    return ''.join(palindrome)
```

This function uses a simple algorithm to find the shortest palindrome. It starts by appending the palindrome character to the empty string, then iterates through each character in the original string. The function checks if the char is a palindrome or not, and if it is palindrome, it breaks the loop and appends the character to the palindrome. The function then joins the string from the palindrome characters to return the shortest palindrome.