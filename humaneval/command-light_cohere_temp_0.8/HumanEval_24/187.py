```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest divisor of the number n that divides evenly.
    """ Example
    regular factors are a 1<divisor<=n, but returns a bigger number for bigger numbers.
    """
    number is a whole number (if it doesn't divide evenly)
    """
    # Handle negative numbers by returning the maximum of that and 1
    if n < 0:
        return max(n, 1)

    # To keep the algorithm simple and efficient, use a loop and 2 numbers
    l, r = 2, n
    div = 1

    while l <= r:
        if n % l == 0:
            # We found a divisor, so return the smallest one greater than it
            return l
        elif n > r:
            break
        r += 1

    # If we reach here, the number does not divide evenly
    # So we must return a bigger number than 1, so it will divide evenly
    return n
```