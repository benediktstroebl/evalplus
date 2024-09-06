```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n-1)}"

# Test the function with different input values
test_string_sequence(0)
test_string_sequence(5)
test_string_sequence(10)
test_string_sequence(15)
```
The function `string_sequence` is designed to generate a string containing space-separated numbers from 0 to n. It employs the method of string concatenation and formatting to achieve this.