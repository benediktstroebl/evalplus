```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if all(i % j == 0 for j in range(1, n)))
``` 
This function uses the Python function `next()` and the `for` loop to iterate over numbers from 1 up to the given number `n`.  The function then checks if the current number divides the number `n` evenly using the `all()`PYX  test, which returns `True` if all the numbers from `j` up to `n` divide `n` evenly.  Finally, the largest number that can be found using this method, which is smaller than `n`.