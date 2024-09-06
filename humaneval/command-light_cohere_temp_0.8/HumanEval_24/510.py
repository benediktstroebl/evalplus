Here is a self-contained Python function that finds the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    while any(x <= n for x in range(1, int(n**0.25)) :
        largest_divisor = x
    return largest_divisor
```

This function uses a simple while loop to find the largest number that divides the given number evenly. The condition `x <= n` ensures that we're looking for divisors smaller than the given number. The function returns the value of the largest divisor found.