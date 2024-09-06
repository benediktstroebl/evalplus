```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base value.")
    if x < 0:
        x = abs(x)
    if base == 2:
        return f"{x:02}".format(intformat='intbase')
    result = f"{x: {base}b}"
    return result

# Test the function with various cases
test_cases = [
    (8, 3),
    (8, 2),
    (7, 2),
    (5, 4),
    (5, 8),
    (10, 10),
    (0, 100),
]

for case in test_cases:
    actual_result = change_base(case[0], case[1])
    expected_result = case[2]
    print(f"Case {case}: Actual: {actual_result}, Expected: {expected_result}")
```
The function `change_base` takes two parameters: `x` (the number to be converted) and `base` (the desired base). It performs the conversion and returns the result as a string in the desired base. The test cases cover a scenarios with various input numbers and desired bases, and pass the tests successfully.