### Largest Divisor of a Number
#### Problem Description
Find the largest divisor of a given number `n` that is smaller than `n`.

#### Code Solution
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.

    Args:
        n (int): The number for which to find the largest divisor.

    Returns:
        int: The largest divisor of n smaller than n.

    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start checking from the largest possible divisor, which is n-1
    for i in range(n - 1, 1, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return it as the largest divisor
            return i

    # If no divisors are found (this should not happen), return 1
    return 1
```
#### Example Use Cases

```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(7))   # Output: 1
```
This script defines a function `largest_divisor` that takes an integer `n` as input and returns its largest divisor smaller than `n`. It iterates from `n-1` down to 2, checking each number to see if it divides `n` evenly. If it does, it returns that number as the largest divisor. If no divisors are found, it returns 1 (which should not happen for positive integers).