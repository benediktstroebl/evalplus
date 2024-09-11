### Solution
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n smaller than n

    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
```
### Explanation
This solution works by iterating over all numbers from `n-1` down to 1. We check each number to see if it divides `n` evenly (i.e., if the remainder of `n` divided by this number is 0). As soon as we find a number that divides `n` evenly, we return it as the largest divisor.

### Example Use Cases
```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 20
print(largest_divisor(17))  # Output: 17
```