```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Input must be numbers")
    return max(divisor(a, b), 1)

def divisor(x: int, y: int) -> int:
    d, i = divmod(x, y)
    return i + d

if __name__ == "__main__":
    a = 25
    b = 15
    print(f"The GCD of {a} and {b} is {greatest_common_divisor(a, b)}")
```