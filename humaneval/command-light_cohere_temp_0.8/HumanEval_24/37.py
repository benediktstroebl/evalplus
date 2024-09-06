Here's a self-contained Python function that finds the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    while n != 1:
        for i in range(1, n // i + 1):
            if n % i == 0:
                return i
        n -= n // 2
    return n
```
This function uses a basic algorithm to find the largest divisor of a given number n, which is to repeatedly divide by all numbers from i = 1 to the square root of n while constantly subtracting by dividing by 2.  The largest number that divides n evenly without leaving a remainder.