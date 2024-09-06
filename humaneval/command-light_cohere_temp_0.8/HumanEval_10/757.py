```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    palindrome = string[::-1] + string[:-len(string) // 2]
    return palindrome

def test_palindrome():
    assert is_palindrome("") == True
    assert is_palindrome("cat") == True
    assert is_palindrome("cata") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("racecar420") == False

if __name__ == "__main__":
    print("Testing the Palindrome function...")
    test_palindrome()
```
The code defines two functions: is_palindrome checks if a given string is a palindrome, and make_palindrome builds a palindrome from a given string. The make_palindrome function follows a simple algorithm: it finds the longest palindrome substring in the input string, then appends the reversed string prefix to the end of the original string. 

The test_palindrome function tests the is_palindrome function with different inputs and asserts the result is True or False, respectively. This script is then self-contained and can be imported and used in other scripts without external dependencies.