```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n+1) if all(x%i == 0 for i in range(1, n))))
```
This Python script defines a function named largest_divisor, which takes an integer n as input and aims to find the largest number that divides evenly into n. The function uses a generator expression and the all() function to achieve this. The generator expression creates a sequence of numbers from 1 to n, and the all() function checks if each element of the sequence is divisible by all numbers from 1 to n. The next() function then returns the result.