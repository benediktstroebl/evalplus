Here's the code:
```python
def largest_divisor(n: int) -> int:
    if n <= 1:
        return n
    result = 1
    while n % 2 == 0:
        n //= 2
        result = max(result, n)
    return result
```
Do you require any additional help with any other aspects of programming or any other topic?