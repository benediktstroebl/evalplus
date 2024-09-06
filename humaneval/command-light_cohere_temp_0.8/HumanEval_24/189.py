```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if n % i == 0)
```
This code defines a Python function called largest_divisor that takes an integer n as input and returns the largest integer that evenly divides n. The code uses the task of generating the list of divisors from 1 up to n, then finds the largest element by using the next() generator. This function is test a list comprehension approach with the range(1, n+1) generator expression, which generates all numbers from 1 up to n. The code uses the reason, the largest number that evenly divides n is 5, which is the largest integer that does not leave a remainder when dividing n by 5.