```python
def largest_divisor(n: int) -> int:
    return n // max([i for i in range(1, n+1) if n % i == 0])
```
This function uses the max function along with list comprehension to find the largest number that divides the given number evenly. It does not use theax efficient way to achieve this.