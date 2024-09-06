```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number less than n that divides it evenly.

    1. If n is divisible by any even number smaller than 1, return 1.
    2. If n is a divisible by any even positive integer k smaller than the square root of n, 
    return k.
    3. If no such divisor exists, return n
    """

# Test cases
assertEqual(largest_divisor(1), 1)
assertEqual(largest_divisor(5), 5)
assertEqual(largest_divisor(17), 5)
assertEqual(largest_divisor(100), 4)
assertEqual(largest_divisor(122), 5)
assertEqual(largest_divisor(156), 6)
assertEqual(largest_divisor(1344), 8)
```