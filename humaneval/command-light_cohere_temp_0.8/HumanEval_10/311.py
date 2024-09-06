```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return string + string[::-1]
    return make_palindrome(string[::-1])

def not_palindrome(string):
    return all([is_palindrome(s) for s in string])

def test_make_palindrome():
    assert make_palindrome("") == '', "Not palindrome: '','"
    assert make_palindrome("cat") == 'catac', "Not palindrome: 'cat'"
    assert make_palindrome("cata") == 'catac', "Not palindrome: 'cata'"
    assert make_palindrome("abcde") == "deabc", "Not palindrome: 'abcde'"
    assert make_palindrome("racecar") == "racecar", "Not palindrome: 'racecar'"

if __name__ == "__main__":
    test_make_palindrome()
```
The above Python code provides a self-contained solution to the problem of creating the shortest palindrome that begins with a given string. The code includes two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` finds the shortest palindrome by recursively appending palindrome substrings until the full prefix is a palindrome. 
The `test_make_palindrome` function tests the function with various inputs and asserts the expected output.