Here's a self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """Return length of given string
    Returns: length of the string"""
    return len(string)

#Test cases
print(strlen('')) # Output: 0
print(strlen('abc')) # Output: 3
print(strlen('hello world')) # Output: 11
print(strlen(' ')) # Output: 1
print(strlen('""')) # Output: 0
```