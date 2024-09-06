```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n - 1)}{n+1}"

#test cases
test_str = string_sequence(5)
print("Test Case 1:", test_str)  # Output: '01234520'

test_str = string_sequence(0)
print("Test Case 2:", test_str)  # Output: '0'

test_str = string_sequence(-5)
print("Test Case 3:", test_str)  # Output: 'FM'

test_str = string_sequence(10)
print("Test Case 4:", test_str)  # Output: '000010'

test_str = string_sequence(0, 20)
print("Test Case 5:", test_str)  # Output: '00000020'
```