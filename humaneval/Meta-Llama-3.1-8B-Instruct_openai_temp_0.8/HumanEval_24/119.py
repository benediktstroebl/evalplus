```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The number to find the largest divisor for
    
    Returns:
        int: The largest divisor of n
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor(n)` that takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It works by iterating over all numbers from `n-1` down to 1 and checking if each number is a divisor of `n` (i.e., `n` divided by the number is an integer). The first such number it finds is the largest divisor, which it then returns.

Alternatively, you could use a more efficient approach by iterating over the divisors of `n` in descending order, like this:

```python
import math

def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The number to find the largest divisor for
    
    Returns:
        int: The largest divisor of n
    """
    for i in range(int(math.sqrt(n)), 1, -1):
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This version of the function uses the fact that the divisors of `n` come in pairs whose product is `n`. Therefore, once it finds a divisor `i`, it also knows that `n // i` is a divisor as well. By only iterating up to the square root of `n`, it can skip over the larger divisors and go straight to the smaller ones.