Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    palindrome = string[:0] + string[-1:]
    while palindrome[0] == palindrome[-1]:
        palindrome = palindrome[1:] + palindrome[:-1]
    return palindrome

def test_make_palindrome():
    assert make_palindrome("") == ""
    assert make_palindrome("cat") == "catac"
    assert make_palindrome("cata") == "catac"
    assert not make_palindrome("asdfgug")  # not a palindrome

def main():
    test_make_palindrome()

if __name__ == "__main__":
    main()
```

The code defines a `make_palindrome` function that creates the shortest palindrome for a given input string, and a related `is_palindrome` function that checks whether a given string is a palindrome. The `main` function tests the Palindrome with some test cases.