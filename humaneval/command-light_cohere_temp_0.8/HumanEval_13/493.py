```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    return min(a, b) // max(divisor(a, b) , 0)

def divisor(a: int, b: int) -> int:
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return i
```