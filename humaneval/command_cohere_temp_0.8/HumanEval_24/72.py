```python
def largest_divisor(n):
    """ Returns the largest divisor of n <= n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function iterates through numbers from 1 to n. If the number is divisible by n, it returns that number, which is always less than or equal to n. 

This algorithm is not the most efficient way to solve this problem as it involves checking all numbers from 1 to n. However, it is the simplest algorithm to understand and execute. 

For better performance, especially for larger input numbers, the following approaches could be taken:
1. Lookup table (prime factorization)
2. Binary search
3. Mathematical approach (e.g., floors of square roots, Newton's method)

If the number n is long enough, a more efficient approach should be considered for optimal performance.