Here is a self-contained Python script with a function that solves the problem of creating a palindrome from a given string:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    # Add palindrome to the string and reverse the prefix.
    palindrome = string + ''.join(reversed(string[: len(string) // 2]))
    return palindrome[::-1]

def test_make_palindrome():
    assert make_palindrome("") == "", "Failed empty string"
    assert make_palindrome("cat") == "catac"
    assert make_palindrome("cata") == "catac"

if __name__ == "__main__":
    test_make_palindrome()
```
The two functions: is_palindrome and make_palindrome, have been defined in this code. The make_palindrome function's function first determines whether the input string is a palindrome, and if not, it returns an empty string. The function then looks for the longest palindrome in the string and creates a new string by concatenating the palindrome to the string's reverse. The final string is then the palindrome.