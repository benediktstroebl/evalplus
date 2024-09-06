Here's a self-contained Python script that defines and implements the function `largest_divisor(n)` to find the largest number that divides a given number `n` evenly:

```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number less than n that divides it evenly"""
    while any(d % n == 0 for d in range(1, int(n**0.25))+ 
        return d
    largest_divisor(n)
```

This function uses a simple while loop to find the largest number that `d` divides `n` evenly, where `d` ranges from 1 to the square root of `n`. The function then returns the largest such divisor.