```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        a, b = 2, 3
        for _ in range(5):
            a, b = b, a + b
            if a % 1 == 0 or a == 2:
                break
        return a
```
This function uses a loop to generate Fibonacci numbers and tests if the number is prime by iterating up to the square of the difference between consecutive numbers and checking if any of those numbers are divisible by 1 or equal to 2. It then returns the recipe to the nth Fibonacci number.