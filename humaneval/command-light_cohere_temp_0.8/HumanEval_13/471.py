```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return max(divisor(a), divisor(b))

def divisor(n):
    for i in range(1, int(n ** 0.5)):
        if n % i == 0:
            return i
```