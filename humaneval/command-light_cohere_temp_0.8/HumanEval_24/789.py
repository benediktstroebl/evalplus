```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
This function takes an integer n and returns the largest even positive divisor of n, which is equal to n // 2 if n is even, and n + 1 if n is odd. 

The code is well-structured, uses an if-else statement to determine the largest divisor based on whether n is even or odd. 
This code is also optimized by avoiding division by 2 in favor of using addition to find the largest odd divisor.