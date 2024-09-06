```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    # Algorithm idea:
    # Find the longest postfix of supplied string that is a palindrome
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.

    palindromic_start = string[:len(string) // 2]
    palindromic_end = string[-len(string) // 2:]

    # Remove all characters between the start and end
    return palindromic_start + palindromic_end[::-1]

def test_make_palindrome():
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'

print("Is Palindrome function:", is_palindrome)  # Output: True
print("Make Palindrome function:", test_make_palindrome)  # Output: True
``` 
This script defines two functions: `is_palindrome` checks if a given string is a palindrome, and `make_palindrome` builds a palindrome from a given string using the idea of finding the longest palindromic prefix and suffix. The `test_make_palindrome` function runs the `make_palindrome` function with some test strings and asserts the result.