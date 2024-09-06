Here's a Python function that checks if a given text is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert text to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    # Check if text is equal to its reverse
    return text == text[::-1]
```
This function first removes all non-alphanumeric characters and converts the text to lowercase to make the comparison case-insensitive and to ignore any punctuation, whitespace, or other non-alphanumeric characters. Then, it compares the cleaned string with its reverse using slicing to determine if it's a palindrome. The tests provided in the problem statement will return True for '', 'aba', and 'aaaaa' and False for 'zbcd'.  This function will provide the same behaviour. 
```python
def test_is_palindrome():
    """
    Tests for is_palindrome function
    """
    assert is_palindrome('')
    assert is_palindrome('aba')
    assert is_palindrome('aaaaa')
    assert not is_palindrome('zbcd')
```
You can add this test function and run it using Python to see if the `is_palindrome` function passes the tests:
```python
test_is_palindrome()
```
This will ensure that the function behaves as expected.