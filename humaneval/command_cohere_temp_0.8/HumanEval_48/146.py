```python
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase to handle case-insensitive palindromes
    text = text.lower()
    # Check if text is empty or has only 1 character, which is trivial palindromes
    if not text or len(text) == 1:
        return True
    # Check if text is a palindrome by comparing characters from beginning and end
    for i in range(len(text) // 2):
        if text[i] != text[-1-i]:
            return False
    return True
```

This function initially checks for empty strings or those with only one character, returning True since they're inherently palindromes. It then iterates through the string's characters, comparing those from the beginning with those from the end, effectively determining whether the string is a palindrome or not. This method is case-insensitive, ensuring accuracy regardless of character cases.

Here's an example of using the function:
```python
# Testing the function
assert is_palindrome('')
assert is_palindrome('aba')
assert is_palindrome('aaaaa')
assert not is_palindrome('zbcd')
```