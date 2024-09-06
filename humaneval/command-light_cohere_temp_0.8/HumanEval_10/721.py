```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = string[::-1] + string[:-len(string)//2]
    return palindrome

def test_make_palindrome():
    assert make_palindrome('') == '', "Invalid input: empty string"
    assert make_palindrome('cat') == 'catac', "Invalid input: not palindrome"
    assert make_palindrome('cata') == 'catac', "Invalid input: not palindrome"
    assert make_palindrome('abcba') == 'aabb', "Invalid input: not a palindrome"

def main():
    print(" palindrome:", is_palindrome('palindrome'))
    print("\nmake_palindrome:", make_palindrome("main functions"))
    test_make_palindrome()

if __name__ == "__main__":
    main()
```

This script defines a function `is_palindrome` that checks if a given string is a palindrome and a function `make_palindrome` that constructs a palindrome from a given string. The function also has a corresponding test function to ensure the correctness of the `make_palindrome` function.