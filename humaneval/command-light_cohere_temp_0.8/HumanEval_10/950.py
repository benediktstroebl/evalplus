```python
def is_palindrome(string: str) -> bool:
    """Test if given string is a palindrome"""
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string"""
    if not string:
        return ''
    lst = []
    for i in range(0,len(string)):
        if i==0 or i==len(string)-1 or string[i] == string[i][::-1]:
            lst.append(string[i])
    else:
        lst.append(string[0:i])
        lst.append(string[i:])
        lst.append(string[::-1][i:])
    return ''.join(lst)
```
The function takes a string as input and checks if it's a palindrome. If it is, it returns True, else False. If the input string is empty, it returns an empty string. If the input string is not a palindrome, it creates a list of substrings that together form a palindrome, and then joins them together into a string. This function efficiently finds the result for making a palindrome.