```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```

This function uses the list comprehension with the "next" function to iterate through numbers from 1 up to the given number, checking if the number divides the given number evenly (i.e., the number is evenly divided by a divisor without remainder).