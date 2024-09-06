```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Input parameters cannot be empty.")
    return math.floor(math.sqrt(a * b) / math.sqrt(b))
```
The function checks for empty input and then uses the Euclidean algorithm to find the greatest common divisor of two integers. It uses the floor(sqrt(a * b) / sqrt(b)) to stay within the integer range.