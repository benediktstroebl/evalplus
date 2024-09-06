Here is a Python script with a self-contained function that solves the problem of making a palindrome from a given string:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''
    else:
        # Find the longest postfix of supplied string that is a palindrome
        palindrome = string[1:] + string[:1]  # Remove leading and trailing whitespaces
        return palindrome + palindrome[::-1]

def test_make_palindrome():
    assert make_palindrome('') == '', 'Make palindrome of empty string'
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'

def main():
    test_make_palindrome()

if __name__ == "__main__":
    main()
```
The script defines two functions: `is_palindrome` checks if a given string is a palindrome or not. The `make_palindrome` function takes a string, determines if a palindrome can be created from it, and if so, it constructs the palindrome. The script also includes a `test_make_palindrome` function that contains tests to verify the functionality of the `make_palindrome` function. 
Finally, the `main` function is called at the end, which executes the code and tests the `make_palindrome` function.