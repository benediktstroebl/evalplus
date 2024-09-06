Here's a self-contained Python function that finds the largest divisor of a given number n:
```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n + 1) if n % i == 0)
```
This function uses the list comprehension technique to iterate from 1 to n (inclusive). Then, it checks if the given number n is divisible by each iteration i, and the first such number is returned, indicating the largest divisor of n. 

This approach has a constant time complexity O(n) as it uses simple arithmetic operations and list comprehension, without needing additional loops or recursive calls.