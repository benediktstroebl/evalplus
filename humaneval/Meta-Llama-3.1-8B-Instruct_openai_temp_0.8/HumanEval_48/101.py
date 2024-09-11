```python
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    
    A palindrome is a string that reads the same backwards as forwards.
    
    Parameters:
    text (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    
    # Remove any whitespace and convert to lowercase
    cleaned_text = ''.join(e for e in text if e.isalnum()).lower()
    
    # Compare the cleaned text with its reverse
    return cleaned_text == cleaned_text[::-1]


# Test cases
if is_palindrome(''):
    print("Empty string is a palindrome")
if is_palindrome('aba'):
    print("aba is a palindrome")
if is_palindrome('aaaaa'):
    print("aaaaa is a palindrome")
if not is_palindrome('zbcd'):
    print("zbcd is not a palindrome")
```
This script will output:
```
Empty string is a palindrome
aba is a palindrome
aaaaa is a palindrome
zbcd is not a palindrome
```
Note that this script also removes any non-alphanumeric characters and converts the string to lowercase before checking if it's a palindrome. This means it will treat "A man, a plan, a canal: Panama" as a palindrome, for example.