```python
def strlen(string: str) -> int:
    """ Return length of given string
    Returns length of string if it's not empty, otherwise returns 0 """
    if not_empty(string):
        return len(string)
    else:
        return 0

def not_empty(string: str) -> bool:
    """ Checks if string is empty """
    return string == ""

# Example test cases
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
print(strlen("abcabc"))  # Output: 3
print(strlen("abcdef"))  # Output: 4
print(strlen(" "))  # Output: 0
print(strlen("A"))  # Output: 1
```