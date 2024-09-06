```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```  This code defines a function called `largest_divisor`, which takes an integer `n` as input and returns the largest divisor of `n`. The function uses a list comprehension and the `next` function to generate all numbers from 1 up to the input number `n`, and checks if the input number is divisible by each of these numbers using the modulo operator `%`.  The `next` function returns the first number in the list that doesn't raise an error when divided by the input number `n`.