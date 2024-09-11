```markdown
### Largest Divisor Function

The `largest_divisor` function finds the largest number that divides a given number `n` evenly, smaller than `n`.

#### Code
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
        n (int): The input number.
    
    Returns:
        int: The largest divisor of n smaller than n.
    
    Examples:
        >>> largest_divisor(15)
        5
    """
    # Start from n-1 and check if each number is a divisor of n
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            # If a divisor is found, return it
            return i
```

#### Usage
```python
# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(17))  # Output: 1
```
This script defines the `largest_divisor` function, which takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates from `n-1` down to 1, checking if each number is a divisor of `n`. If a divisor is found, it is immediately returned. The script also includes example usage and test cases to demonstrate the function's behavior.