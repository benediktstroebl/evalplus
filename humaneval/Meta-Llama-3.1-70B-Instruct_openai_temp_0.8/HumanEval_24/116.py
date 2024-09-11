```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n that is smaller than n.
    """
    
    # Start checking from n-1 because n is not a valid divisor according to the problem
    for i in range(n-1, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # If it is, return it immediately because we're checking in descending order
            return i

# Test the function
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(17))  # Expected output: 1
print(largest_divisor(30))  # Expected output: 15
```

This script defines the `largest_divisor` function that takes an integer `n` and returns the largest number that divides `n` evenly and is smaller than `n`. The function iterates from `n-1` down to `1` and returns the first number that is a divisor of `n`. The test cases are also provided to verify the correctness of the function.