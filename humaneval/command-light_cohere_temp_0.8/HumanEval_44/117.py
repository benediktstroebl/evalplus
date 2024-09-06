```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10
    per convention.
    """
    format: [base] -> {integer -> string conversion}
    """
    return '{:02}'.format(int(x), base)

# Example Test Cases
test_cases = [
    (8, 3),
    (8, 2),
    (7, 2),
    (10, 1),
    (10, 3),
    (100, 2),
    (100, 5),
    # Add more test cases here...
]

# Loop through test cases and print results
for x, base in test_cases:
    actual_result = change_base(x, base)
    print(f"Test case {x}, base {base}: {actual_result}")
```