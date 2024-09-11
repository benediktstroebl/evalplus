### Largest Divisor Finder
#### Problem Description

Find the largest number that divides a given number `n` evenly, smaller than `n`.

#### Solution

```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The largest divisor of n smaller than n.
    """
    
    # Start from the second largest possible divisor (n // 2)
    for i in range(n // 2, 0, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            return i
    
    # If no divisor is found, return 1 (1 is a divisor of all numbers)
    return 1

# Example usage
print(largest_divisor(15))  # Output: 5
```

#### Explanation

This function starts from the second largest possible divisor of `n` (which is `n // 2`) and checks each number downwards. If it finds a divisor, it immediately returns that value. If no divisor is found, it returns 1, which is a divisor of all numbers.