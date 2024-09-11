### Largest Divisor of a Number
#### Problem Description
Find the largest number that divides a given number `n` evenly, smaller than `n`.

#### Solution
```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number

    Returns:
        int: The largest divisor of n smaller than n

    Examples:
        >>> largest_divisor(15)
        5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1  # Return 1 if n is a prime number

# Test the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(17))  # Output: 1
print(largest_divisor(24))  # Output: 12
```

#### Explanation
The script uses a simple iterative approach to find the largest divisor. It starts from `n-1` and checks each number if it divides `n` evenly (i.e., `n % i == 0`). The first such number encountered is the largest divisor. If no such number is found (i.e., `n` is a prime number), the function returns 1.