A simple solution is to make the first letter of each word a reverse. To achieve this such` create a palindrome by capitalizing the first letter of each word and then reverse the whole string. 

```python
def make_palindrome(string: str) -> str:
    """
    Returns:
        str: The shortest palindrome of the input string.
    """
    # Find the longest palindrome postfix
    # Capitalize first letter of each word
    # Reverse the whole string
    return ''.joinem(string[0]) + string[::-1]
```