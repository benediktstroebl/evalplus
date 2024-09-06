```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not any(n % d)))
 ```

This function uses the next() function with a generator expression to create a generator that returns integers from 1 to n. Then, the code checks if there are any divisors of n by looping over the generator and checking if n is not divisible by the current number.