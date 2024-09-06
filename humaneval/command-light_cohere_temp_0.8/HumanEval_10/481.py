Here is a Python script that solves the problem of converting a string to palindrome:
```python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    if not string:
        return ""
    # Find the longest postfix of supplied string that is a palindrome
    palindrome = string[:string.find_palindrome()]
   
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return palindrome + string[-palindrome::length]

# Unit tests
def test_make_palindrome():
    assert make_palindrome("") == "", "Palindrome is empty for an empty string"
    assert make_palindrome("bob") == "bobbob", "Could not make palindrome for \"bob\""
    assert make_palindrome("caca") == "cacaaca", "Could not make palindrome for \"caca\""
    assert make_palindrome("racecar") == "racecarrev", "Could not make palindrome for \"racecar\""

if __name__ == "__main__":
    test_make_palindrome()
```
This Python script defines two functions: `is_palindrome` and `make_palindrome`. The `is_palindrome` function checks if a given string is a palindrome, returning a boolean value. The `make_palindrome` function creates a palindrome by finding the shortest palindromic substring within the original string.