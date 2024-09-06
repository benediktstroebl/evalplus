Here's a Python function that checks if a given string is a palindrome:
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    return text == text[::-1]
```
This function removes non-alphanumeric characters and converts the text to lowercase to make the comparison case-insensitive and to accommodate for different letter cases. It then checks if the cleaned string is equal to its reverse. The 'str.lower()' and 'str[::-1]' methods are used for string conversion and reversing respectively. The function returns True if the string is a palindrome and False otherwise. 
```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase and remove all non-alphanumeric characters
    text = ''.join(c for c in text if c.isalnum()).lower()
    return text == text[::-1]

```
This function can be called with different strings to determine if they are palindromes or not. 

For example:
```python
# Call the function with different strings
print(is_palindrome(''))
print(is_palindrome('aba'))
print(is_palindrome('aaaaa'))
print(is_palindrome('zbcd'))
```
This will give the following output:
```
True
True
True
False
```
The function passes the given tests and should work correctly for validating palindromes.