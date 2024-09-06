```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be provided")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Input must be integers")
    if a <= 0 or b <= 0:
        raise ValueError("Both numbers must be positive")

    # Calculating GCD using recursive approach
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

    return 0
```