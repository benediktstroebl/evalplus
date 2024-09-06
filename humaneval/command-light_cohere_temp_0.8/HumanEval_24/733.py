Here is a Python script with a self-contained function that finds the largest divisor of a given number:

```python
def largest_divisor(n: int) -> int:
    # Initialize the largest divisor
    l = n
    while n % l == 0:
        l += 1
    return l
# Test case 1
assert largest_divisor(15) == 5
# Test case 2
assert largest_divisor(27) == 3
```

This code defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest integer that divides `n` evenly, smaller than `n`. It uses a while loop to find such divisor and updates the largest divisor until `n` is divisible by the current value of `l`.