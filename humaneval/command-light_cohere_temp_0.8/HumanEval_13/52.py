```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both inputs must be positive numbers")
    return abs(b) if a > b else b
def test_greatest_common_divisor() -> None:
    try:
        result = greatest_common_divisor(3, 5)
        print(result)
        result = greatest_common_divisor(25, 15)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    return None
```