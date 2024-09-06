Here's a Python function that checks if a given text is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    
    # Check if text is same when reading backwards
    return text == text[::-1]
```
This function first removes all non-alphanumeric characters and converts the text to lowercase to make the comparison case-insensitive and to ignore differences in punctuation, whitespace, and other non-alphanumeric characters. It then checks if the cleaned up version of the text is the same when reading forwards and backwards. The `::bool` annotation in the function signature is used to specify the return type of the function as `bool`. This function can be used to correctly determine if a string is a palindrome or not. 

Here are some usage examples that demonstrate the behavior of the function:
```python
>>> is_palindrome('')
True
>>> is_palindrome('aba')
True
>>> is_palindrome('aaaaa')
True
>>> is_palindrome('zbcd')
False
``` 
This shows that the function correctly identifies the empty string, reversed strings, and non-reversed strings as palindromes or not, based on their behavior. In the final example, the non-alphanumeric character 'z' is converted to 'z' in the cleaned text, and 'cd' becomes 'cd', so the resulting text is 'zbcd' which is not a palindrome. The function correctly returns `False` in this case.  This matches the desired behavior for the function as outlined in the problem statement.