```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = string[:string.find(str.translate(str))][::-1]
    return palindrome + string[len(palindrome):]
```
The above Python script defines a function is_palindrome that checks if a given string is a palindrome or not, and a function make_palindrome that constructs the shortest palindrome using the algorithm. This algorithm idea is simple: find the longest palindrome of the prefix and append the reverse of the found palindrome.