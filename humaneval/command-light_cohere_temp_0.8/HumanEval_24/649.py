Here is a Python script with a self-contained function that finds the largest number which divides a given number `n` evenly:

```python
def largest_divisor(n: int) -> int:
    """ Returns the largest number that divides n evenly, smaller than n."""
    while n % 2 == 0:
        n -= 1
    return n
```

This function checks for oddness of the number and then repeatedly removes the 2 from the number until the number is odd, at which point the largest odd divisor is the number itself.