```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if not(n % i):
    ```
This Python function, largest_divisor, accepts an integer n and quickly identifies the largest integer which evenly divides n without leaving a remainder. 

This function employs the built-in function `next()` to generate a sequence of numbers from 1 up to n, and then checks whether n is divisible by each of these numbers. It utilizes the's `next()` to iterate through these numbers, avoiding the need for an explicit loop.

The `next()` function returns the first element of the generated sequence which meets the condition, ensuring that the largest divisor is returned without delay.