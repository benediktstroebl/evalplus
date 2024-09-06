Here is a self-contained Python script that defines a function largest_divisor(n) which finds the largest number that divides a given number n evenly:

```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```

The function uses the next() function together with a generator expression to iterate through the numbers from 1 to n. The function returns the result the number that is both greater than 1 and also divides the given number n evenly.