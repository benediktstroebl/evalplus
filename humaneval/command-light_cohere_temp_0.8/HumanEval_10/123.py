```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(input_string):
    if not_palindrome(input_string):
        return ""

    palindrome = input_string[-1:]
    while palindrome != input_string[0]:
        palindrome += input_string[1:]
        input_string = input_string[1:] + input_string[0]
    return input_string

def test_make_palindrome():
    assert make_palindrome("") == ""
    assert make_palindrome("cat") == "catac"
    assert make_palindrome("cata") == "catac"

if __name__ == "__main__":
    test_make_palindrome()
```
The code defines a function `is_palindrome` that checks if a given string is a palindrome and another function `make_palindrome` that constructs a palindrome from a given string. The `test_make_palindrome` function verifies the functionality of the `make_palindrome` function with a few test cases.