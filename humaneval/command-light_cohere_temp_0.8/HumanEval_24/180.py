```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n - 1
```
This function takes an integer n and returns the largest integer that divides n evenly, i. previous greatest divisor, which is always the largest number that is less than n, and this is achieved by checking the remainder when n is divided by 2. The function then returns the largest number that satisfies this property.