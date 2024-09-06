```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else(str.isupper(c)) else c.isupper() else(c)) for c in string)

# Example usage
test_string = "Hello world!"
assert flip_case(test_string) == "hELLO"
```