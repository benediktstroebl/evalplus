```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    Args:
        n (int): The input number
    
    Returns:
        int: The largest divisor of n
    """
    # Start from n-1 and decrement until we find a divisor
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i

# Example usage:
print(largest_divisor(15))  # Output: 5
```
This script defines a function `largest_divisor` that finds the largest number that divides the input number `n` evenly, smaller than `n`. It uses a loop to iterate from `n-1` down to 1, checking if each number is a divisor of `n`. As soon as it finds a divisor, it returns that number.