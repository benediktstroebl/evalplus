```python
def largest_divisor(n: int) -> int:
    return next((x for x in range(1, n+1) if all(x % n == 0)))
```
The function uses the Python next() function with a generator expression. This approach generates the particular number from 1 to n, and for each number, checks if the number is divisible by n without remainder. The loop continues until the generator expression evaluates to False, indicating that no such number exists. 

The function effectively finds the largest such divisor of n that is less than n itself.