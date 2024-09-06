```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

# Test the function with different values of n
test_string_sequence = string_sequence(0)
assertEqual(test_string_sequence, '0')
test_string_sequence = string_sequence(5)
assertEqual(test_string_sequence, '0 1 2 3 4 5')
```
The function will return a string containing space-delimited numbers starting from 0 to n inclusive. 

The above function is simple and uses the Python syntax to create a function and an assertion.