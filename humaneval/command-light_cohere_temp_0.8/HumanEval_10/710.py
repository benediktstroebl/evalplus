Here is a Python script that contains a self-contained function to solve the problem of creating a palindrome:
```python
def is_palindrome(string):
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ""

    new_str = []
    while True:
        # Find the longest palindrome or a non-palindrome char
        index = string.index(' ', 0, -1)
        palindrome = string[:index] + string[index + 1:]

        # Check if the palindrome is empty or the same as the input
        if palindrome == string:
            break

        # Append the reverse of the prefix and the palindrome
        new_str.append(palindrome[::-1])
        new_str.append(' ')

    new_str.append(string[1:])
    return ''.join(new_str)

def test_palindrome():
    assert is_palindrome("") == True
    assert is_palindrome("cat") == True
    assert is_palindrome("cata") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("ll") == False

print(make_palindrome(""))
print(make_palindrome("cat"))
print(make_palindrome("cata"))
print(make_palindrome("hello world!"))
print(make_palindrome("ll!"))

print(test_palindrome())
```

This script provides a function to check if a given string is a palindrome and another function to create a palindrome given a string.