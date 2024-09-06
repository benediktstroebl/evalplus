```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    palindrome = []
    while True:
        if is_palindrome(string[-1:]) and string[:-1] == string[-1:]:
            palindrome.append(string[1:])
            break
        else:
            palindrome.append(string[1:])
            reverse = string[::-1]
            while reverse:
                palindrome.append(reverse[1:])
                reverse = incent(reverse)
    return ''.join(palindrome)
```
The above code defines a function make_palindrome that takes a string and returns a palindrom of the string. It uses a technique to find the shortest palindrome using the is_palindrome function.