```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n+1) if not divmod(i, n).
    ```

This code defines a function called `largest_divisor` that takes an integer n as input and returns the largest integer that divides n without a remainder. The code uses theutilizes the Python's built-in `range` function to generate all numbers from 1 up, and the `divmod` function to check if each number divides n evenly. The `next` function is then used to skip over the numbers that do not meet the condition and return the first number that does.