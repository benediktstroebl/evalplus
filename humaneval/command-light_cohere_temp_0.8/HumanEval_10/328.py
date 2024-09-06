A self-contained Python function that solves the palindrome generation problem with the provided tests is below:
```python
def is_palindrome(string): 
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ''
    lst = []
    while True:
        is_palindrome = True
        for i in range(len(string)):
            if string[i] != string[len(string) - i - 1]:
                is_palindrome = False 
                break
        if is_palindrome:
            lst.append(string[i:])
        else:
            break
    for i in range(len(string) - 1, 0, -1):
        lst.append(lst[i])[::-1]
    return ''.join(lst)
```

The code defines two functions: `is_palindrome` checks if a given string is a palindrome or not, and `make_palindrome` finds the shortest palindrome that begins with a given string.

The `make_palindrome` function uses a loop to find the longest postfix of the string that is a palindrome. It then appends the one by one, reversing each one, to create the palindrome.