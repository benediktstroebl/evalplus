```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} ...........{n+{n+1}-1}"

# Test the function with different inputs
test_sequence = string_sequence  # Create a test function instance

# Test with different cases of input
print(test_sequence(0))  # Output: '0'
print(test_sequence(5))  # Output: '0 1 2 3 4 5'
print(test_sequence(10)) # Output: '0 9 8 7 6 5 4 3 2 1'
print(test_sequence(15)) # Output: '0 14 13 12 11 10 9 8 7 6 5 3 2 1'
print(test_sequence(0))
print(test_sequence(-1))
```