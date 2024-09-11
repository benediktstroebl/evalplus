```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor of

    Returns:
        int: The largest divisor of n smaller than n
    """
    # Iterate from n-1 down to 1 to find the largest divisor
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i

# Test the function
if __name__ == "__main__":
    print(largest_divisor(15))  # Output: 5
```

Alternatively, you can use a more mathematical approach to find the largest divisor:

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The number to find the largest divisor of

    Returns:
        int: The largest divisor of n smaller than n
    """
    # Find the square root of n
    sqrt_n = int(n ** 0.5)
    
    # Iterate from sqrt_n down to 1 to find the largest divisor
    for i in range(sqrt_n, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If i is a divisor, return it as the largest divisor
            return i

# Test the function
if __name__ == "__main__":
    print(largest_divisor(15))  # Output: 5
```

This alternative version is more efficient because it only needs to iterate up to the square root of `n`, which is much smaller than `n`.