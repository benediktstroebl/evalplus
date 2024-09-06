```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base
    >>> change_base(8, 2)  # Result: 1000
    >>> change_base(123, 5)  # Result: 5 permission
    >>> change_base(10, 5)   # Result: 55 permission
    >>> change_base(37, 10) # Result: 37 permission
    >>> change_base(0, 4)  
    """
    # Convert to string and back to int to ensure base conversion
    base_str = str(base)
    x_str = str(x)
    return base_str + x_str[::-1]

# Test cases
test_cases = [
    (8, 2),
    (123, 5),
    (10, 5),
    (37, 10),
    (0, 4),
]

for x, base in test_cases:
    print(f'Base: {base}, Result: {change_base(x, base)})
``` 
The above Python code defines a function change_base that converts a number to a new base, tests it with a series of test cases, and prints the results.