```python
def flip_case(string: str) -> str:
    return ''.joinCaseInsensitive(string)

# Test cases
assert flip_case('Hello') == 'hELLO'
assert flip_case('HELLO') == 'oLLo'
```
This function transforms a given string into lowercase by applying case-insensitive conversion, ensuring that both lowercase and uppercase characters are converted to their counterparts.