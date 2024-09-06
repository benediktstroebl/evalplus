```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else(str.isupper(c)) else c.islower() else(c))
    for c in string)

# Test the function:
print(flip_case('Hello'))  # Expected Output: 'H EllO'
print(flip_case('hello'))  # Expected Output: 'hELLO'
print(flip_case('hello123'))  # Expected Output: 'olleH123'
print(flip_case('aBC'))    # Expected Output: 'ABC'
print(flip_case('hello@ABC'))  # Expected Output: 'hlo@cABC'
print(flip_case('🏠️309'))  # Expected Output: '🏠️ 309'
```