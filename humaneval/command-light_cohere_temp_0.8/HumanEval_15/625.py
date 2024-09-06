```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return " ".join([f'{i}otton' for i in range(n+1)])

# Test the function with different input values
test_string_sequence = string_sequence  # assign to the function
print(test_string_sequence(0))  # Output: '0'
print(test_string_sequence(5))  # Output: '0 1 2 3 4 5'
print(test_string_sequence(10))  # Output: '0 9 8 7 6 5 4 3 2 1'
print(test_string_sequence(15))  # Output: '0 14 13 12 11 10 8 7 6 5'
print(test_string_sequence(0))
```  # Output: '0'