```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string: return ''
    str1 = []
    while True:
        pal = False
        for i in range(0, len(string) // 2):
            if string[i] == string[len(string) - i - 1]:
                pal = True
                break
        if pal:
            break
        str1.append(string[::-1])
    return ''.join(str1)
```
This code defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` generates the shortest palindrome from a given string. 

The `make_palindrome` function uses a simple algorithm to create the palindrome. The function checks if the string is empty, then returns an empty string. It then initializes a string variable `str1` as an empty list. 

The function enters a `while` loop where it repeatedly checks if each character in the string is the same as its corresponding reverse. When it finds a character that is a palindrome, it breaks out of the loop and appends the reverse of the found palindrome to the `str1` list. 

Finally, the function joins the elements in `str1` into a string and returns the result.