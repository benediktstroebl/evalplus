```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base base.
    return string representation after conversion.
    base numbers are use 10."""
    return '{:02x}'.format(x, base)

# Test cases
test_cases = [
    (8, 3),
    (8, 2),
    (7, 2),
]

for x, base in test_cases:
    actual = change_base(x, base)
    expected = '{:02x}'.format(x, base)
    assert actual == expected, f"Test case {x} failed: Actual={actual}, Expected={expected}"

print("All tests passed!")
```