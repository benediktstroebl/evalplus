```python
def strlen(string: str) -> int:
    """ Return length of given string
        Returns 0 if string is empty"""
    if not string:  # Empty string returns 0
        return 0
    length = 0
    for i in range(1,len(string)+1):
        if string[i-1] == string[i]:
            length += 1
    return length
# Test cases
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
print(strlen('Welcome Aida!'))  # Output: 10
```