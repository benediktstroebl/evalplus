```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
This function uses the floor division operator (//) to find the largest number that evenly divides the given number, smaller than the input n, which guarantees that the result is always an integer. 

Please note that the approach of checking for odd or even divisors by using conditional statements is a common and efficient method.