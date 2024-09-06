Here's a self-contained Python function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
assertEqual(strlen(''),             0)
assertEqual(strlen(' '),             0)
assertEqual(strlen('abc'),        3)
assertEqual(strlen('abcde'),        5)
assertEqual(strlen(''),           0)
assertEqual(strlen('      '),        8)

# Example usage
string = 'abc'
print(strlen(string))  # Output: 3
```
This function returns the length of the given string, which is the number of characters in the string.