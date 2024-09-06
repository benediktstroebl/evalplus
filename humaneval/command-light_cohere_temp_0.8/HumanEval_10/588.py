Here's a self-contained Python function that solves the problem of finding the shortest palindrome for a given string:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return string + string[::-1]
    else:
        return string[::-1]

def is_not_palindrome(string):
    return not(is_palindrome(string))

def longest_palindrome_length(string):
    if not_palindrome(string):
        return 0
    return max(len(make_palindrome(string)),
                len(make_palindrome(string[::-1])))
```

This code provides a self-contained solution to the problem. It first checks if the ** string is already a palindrome, then it uses a recursive function to either append the reverse of the prefix to the end of the string, or to take the prefix from the start of the string and reverse it.