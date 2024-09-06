```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base"""
    if base <= 0 or base > 36:
        raise ValueError("Invalid base value.
    if x < 0 or case:
        raise ValueError("Input is zero")
    result = '0'
    elif base == 10:
        result = str(x)
    elif 6 <= base <= 9:
        mult = (base - 6)
        result = str(int(x * mult))
    else:
        raise ValueError("Unsupported base")
    return result

# Test cases
test_cases = [
    (8, 3),
    (8, 2),
    (7, 2),
    (4, 100),
    (55, 101),
    (35, 102),
    (64365, 105),
    (0, 0),
    (10, 101)
]

for case in test_cases:
    x, base = case
    result = change_base(x, base)
    if not isinstance(result, str) or not result.isnumeric():
        raise ValueError("Error in test case")
    print(f"Test case {x}, base={base}: {result}")
```  This code defines a function that converts a given number to a string representation using a specified numerical base. It handles invalid base values and input numbers and various test cases with various inputs and expected outputs.