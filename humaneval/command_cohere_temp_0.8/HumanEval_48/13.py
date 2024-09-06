Here's a Python script with a self-contained function that solves the problem of checking if a given string is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if the reversed string matches the original string
    return text == text[::-1]
```
This function leverages these steps to determine palindrome:
-   Convert the input string to lowercase using the `.lower()` method.
-   Remove any non-alphanumeric characters using a list comprehension.
-   Directly compare the modified string with its reverse using slicing.

The tests included demonstrate the function's behavior:
```python
test_palindrome = {
    ('', 'aba', 'aaaaa', 'zbcd'),
    ('Hello', 'world', 'madam, I'm Adam', 'racecar'),
}
for test_string, expected in test_palindrome:
    assert is_palindrome(test_string) == expected
```

The first element of each tuple is the input string, and the second element is the expected result of the `is_palindrome` function. The test succeeds if the actual output of the function matches the expected output.