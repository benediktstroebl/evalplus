Here is a Python script with a self-contained function that solves the problem:
```python
def is_palindrome(string): 
    return string == string[::-1]

def make_palindrome(string):
    if not_palindrome(string):
        return ''

    palindrome = string[:string.find(str.sub(str.r())]
    _ distinctive palindrome
   
    return palindrome

# Function test
def test_make_palindrome():
    input_str = "cascnocat"
    expected_str = "catorsac"
    result = make_palindrome(input_str)
    assert result == expected_str, "Result is not the expected palindrome"
```
This code defines two functions: is_palindrome checks if a given string is a palindrome, and make_palindrome finds the shortest palindrome that begins with a supplied string. The test_make_palindrome function tests the make_palindrome function with different input strings, and it asserts that the result is the expected palindrome.