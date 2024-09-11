```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n.
    """
    # Start checking from n - 1, because we want a divisor smaller than n
    for i in range(n - 1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
```

This script defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides `n` evenly, which is smaller than `n`. The function iterates through numbers smaller than `n` in descending order and checks if each number is a divisor of `n`. As soon as it finds a divisor, it returns that number.