```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n + 1) if not divmod(i, n).
    ```

The function uses the divmod() function, which returns the remainder when dividing a number n by i. The function then uses the `next()` function to iterate over numbers starting from 1 to the number n, checking if the divmod operation returns 0. If it does, the loop terminates because n is a multiple of i, meaning that i is a multiple of n, but smaller.

This function is self-contained and can be used to find the largest divisor of a given number n.