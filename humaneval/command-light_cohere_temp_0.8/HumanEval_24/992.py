```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
This function determines the largest divisor of the provided number 'n' that evenly divides it, smaller than the input number. The function utilizes the only odd numbers greater than 1 as the largest divisors of even numbers, while it returns n + 1 as the largest divisor of numbers that are odd.

This is a self-contained Python function that solves the problem of finding the largest number that divides a given number evenly, smaller than the given number, in just one expression, which is good for readability and reducing code complexity.