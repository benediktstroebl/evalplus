```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs must be a positive integer")
    return max((i for i in range(1, max(a, b)) if a % i == 0 and b % i == 0))
```
I hope this helps you to solve the problem of finding the greatest common divisor of two numbers in a markdown code block, with clear and concise code.