```python
def string_sequence(n: int) -> str:
    if n <= 0:
        raise ValueError("n should be a positive integer")
        
    result = [f'0 {i+1}' for i in range(n+1)]
    return ' '.join(result)

# Test cases
test_string_sequence = str_sequence(0)
assert test_string_sequence == '0'

test_string_sequence = str_sequence(5)
assert test_string_sequence == '0 1 2 3 4 5'

# Run the above function and tests to check the functionality.
 ```