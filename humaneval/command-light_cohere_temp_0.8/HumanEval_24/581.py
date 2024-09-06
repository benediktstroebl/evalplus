```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not any(n % d == 0)))
```
This code defines a function called largest_divisor, which takes an integer n as input and returns the largest integer that divides n without a remainder. The function achieves this purpose by using the `next` function, which generates the numbers from 1 to n, and uses the `not any` function to check if there is a remainder when dividing. 
This is a self-contained solution, as it only uses built-in functions and does not require any additional imports or external functions.