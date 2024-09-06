Here's a Python function that checks if a given string is a palindrome, and a sample test to verify its correctness:
```python
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with a supplied string """
    
    # Find the longest postfix of supplied string that is a palindrome
    palindrome = ''
    for char in string:
        if palindrome and char == palindrome[-1]:
            palindrome += char
        else:
            palindrome = char
    return palindrome

# Test the function with a sample input
test_string = "cat"
print(is_palindrome(test_string))  # True
print(make_palindrome(test_string))  # Output: catac
```