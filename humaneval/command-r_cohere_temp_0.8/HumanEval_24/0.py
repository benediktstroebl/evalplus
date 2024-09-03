```python
def largest_divisor(n: int) -> int:
""" For a given number n, find the largest number that divides n evenly, smaller than n.

Args:
    n (int): Number to find the largest divisor for

Returns:
    int: Largest number that divides n evenly
"""
    # Initialize the largest divisor to 1
    max_divisor = 1

    # Iterate through potential divisors
    for i in range(2, n):
        # Check if n is divisible by i
        if n % i == 0:
            # Update the max divisor if a larger divisor is found
            max_divisor = i

    return max_divisor
```