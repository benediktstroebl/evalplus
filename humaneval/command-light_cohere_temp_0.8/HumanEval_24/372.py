```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not divmod(d, n).
    # returns 1 if d divides n exactly, 0 otherwise
    ),   0)
``` 
This function employs a generator expression and the `next()` function to iterate over the numbers from 1 to `n`, inclusive. It then checks if each number in this range divides `n` exactly without a remainder using the `divmod()` function, which returns 1 if the divisor divides the dividend exactly, 0 otherwise. The loop terminates when the largest such divisor is returned, which is guaranteed to be less than n due to the iterator's range.