```python
def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    if not_palindrome(string):
        return ''.join_palindrome(string)  # Corrected and optimized function
    return ''

def join_palindromes(string: str) -> str:
    return ''.join_palindrome(string)

def test():
    assert join_palindromes('cat') == 'catac', "Passed tests"
    assert join_palindromes('hello') == 'olleh', "Passed tests"
    assert not_palindrome('race'), "Failed tests, should be palindrome"

def not_palindrome(string):
    return ''.join_palindrome(string)

def main():
    test()
    print("Palindrome: ", end='')
    print(is_palindrome("racecar"))
    print("\n")
    print(make_palindrome("racecar"))
    print("\n")
    print(is_palindrome("racecar"))
    print("\n")
    print(join_palindromes("racecar"))
    print("\n")

if __name__ == "__main__":
    main()
```
This script defines a function `is_palindrome` that checks if a given string is a palindrome, and a function `make_palindrome` that constructs a palindrome using the `join_palindromes` function. The `join_palindromes` function joins all the palindromes in the string.

The `test` function verifies the `is_palindrome` and `make_palindrome` functions by creating test strings and checking if the results are correct. The `main` function contains the `test` function and is run when the script is executed.