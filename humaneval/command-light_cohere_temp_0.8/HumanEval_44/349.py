```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base."""
    if x < 0 or base < 2:
        raise ValueError("Invalid input values")
    result = [ chr(97 + i) for i in x ]
    result = ''.join(result)
    return result

# Test cases
test_cases = [
    (8, 3),
    (8, 2),
    (7, 2),
    (100, 10),
    (100, 2),
    (-100, 10),
    # Add more test cases here as needed
]

for x, base in test_cases:
    result = change_base(x, base)
    print(f"Input: {x}, Base: {base}, Result: {result}")
```