```python
def largest_divisor(n: int) -> int:
    return n // max(x for x in range(1, n+1) if x % n == 0)
```
The function largest_divisor takes an integer n as input and returns the largest integer that divides n exactly. The function uses a efficient approach to find such number using the concept that the largest number which divides n exactly is the maximum value of x such that x divides n evenly.