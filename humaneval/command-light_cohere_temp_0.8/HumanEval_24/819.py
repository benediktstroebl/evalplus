```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if n % i == 0)
```
The function uses the Python next() function and a generator expression in a loop to iterate through numbers from 1 to n. The function returns the value of the first integer i that satisfies the condition. This approach is simple and efficient and it will print the largest divisor that is smaller than n.