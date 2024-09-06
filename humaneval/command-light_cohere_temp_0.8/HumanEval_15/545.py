```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} ".center(n)

# Test the function with different values of n
test_string_sequence(0)
test_string_sequence(5)
test_string_sequence(10)
test_string_sequence(15)
```
The code defines a Python function `string_sequence` that generates a string containing numbers with spaces, starting from 0 and ending just before the given `n`. The function uses string formatting to center the numbers and then inserts `n` spaces before and after the numbers. It can be used with a variety of test cases.