```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive."""
    return f"0 {n}{' ' * (n-1)}"
    
# Test cases
test_str = string_sequence(0)
assert test_str == '0'
test_str = string_sequence(5)
assert test_str == '0 1 2 3 4 5'
    
# Main function call
print(string_sequence(10))
```