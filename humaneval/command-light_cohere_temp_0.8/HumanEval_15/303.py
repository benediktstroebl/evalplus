```python
def string_sequence(n: int) -> str:
    if not n:
        raise ValueError("Input cannot be zero")
    return " ".join([f'{i+1}' for i in range(n)])

#Test case 0
test_string_sequence(0)
# Output: '0'

#Test case 1
test_string_sequence(5)
# Output: '0 1 2 3 4 5'

#Test case 2
test_string_sequence(-5)
# Expected ValueError: Input must be a positive integer
```