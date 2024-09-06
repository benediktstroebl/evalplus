```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input is zero.")
    while a != 1 or b != 1:
        if a % b == 0:
            a, b = b, a // b
        else:
            break
    return min(a, b)

# Test the function
3  # Intentionally smaller number
# 5
25  # Larger number to test for correctness
15
```