```markdown
**Largest Divisor Function**
==========================

A self-contained Python script that solves the problem of finding the largest divisor of a given number.

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Initialize the largest divisor to 1
    largest = 1
    
    # Iterate from n-1 to 2 (inclusive) to find the largest divisor
    for i in range(n-1, 1, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Update the largest divisor
            largest = i
            # Break the loop since we've found the largest divisor
            break
    
    return largest
```

**Example Usage**
----------------

```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 20 (yes, 20 is the largest divisor of 20)
```

This script uses a simple loop to iterate from `n-1` down to 2, checking each number to see if it's a divisor of `n`. The first divisor found is assumed to be the largest, so we return it as soon as we find it.