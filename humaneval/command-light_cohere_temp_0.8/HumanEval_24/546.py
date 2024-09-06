```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d))
 ```

This code defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest integer that divides evenly into `n`. The function uses a list comprehension and the `next()` function to iterate through the numbers from 1 to `n` and checks if the current number `d` is a divisor of `n` using the `not n % d` condition. 
 then returns the final number in the list comprehension.