### Largest Divisor
#### Problem Statement

For a given number `n`, find the largest number that divides `n` evenly, smaller than `n`.

#### Solution
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n smaller than n.
    
    Examples:
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
```
### Explanation

*   We iterate through all numbers from `n-1` down to `1` using a for loop.
*   Inside the loop, we check if `n` is divisible by the current number `i` using the modulus operator (`n % i == 0`).
*   If `n` is divisible by `i`, we return `i` as the largest divisor.
*   This approach ensures that we find the largest divisor smaller than `n`.

### Example Use Cases

You can use this function as follows:

```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(10))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(1))   # Output: 1
```