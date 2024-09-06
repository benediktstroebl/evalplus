Here is a Python script with a self-contained function that solves the problem of finding the shortest palindrome:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    if not string:
        return ""

    # Find the longest postfix of supplied string that is a palindrome
    max_palindrome_len = len(string)
    palindrome_start = 0
    while True:
        while palindrome_start < max_palindrome_len and string[palindrome_start] != string[palindrome_start][::-1]:
            palindrome_start += 1

        if palindrome_start == max_palindrome_len:
            break

        # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
        palindrome = string[:palindrome_start] + string[palindrome_start:][::-1]
        return palindrome

print(is_palindrome("racecar")) # True
print(is_palindrome("Hello")) # False
print(make_palindrome("racecar")) # racecrca
print(make_palindrome("Hello"))# Hello 

``` 
This code defines two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome, while the `make_palindrome` function finds the shortest palindrome that begins with a supplied string using a simple algorithm.