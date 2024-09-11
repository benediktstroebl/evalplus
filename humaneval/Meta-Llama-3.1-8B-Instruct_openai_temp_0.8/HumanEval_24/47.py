```markdown
### Largest Divisor Function

This function finds the largest number that divides a given number `n` evenly, smaller than `n`.

#### Code
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
    # Initialize the largest divisor to 1
    largest_div = 1

    # Iterate from n-1 to 2 (inclusive)
    for i in range(n - 1, 1, -1):
        # Check if i is a divisor of n
        if n % i == 0:
            # Update the largest divisor
            largest_div = i
            # Break the loop as we found the largest divisor
            break

    return largest_div
```

#### Example Use Cases
```python
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(7))   # Output: 1
```

#### Notes
The function uses a loop to iterate from `n-1` down to 2, checking each number to see if it's a divisor of `n`. The loop breaks as soon as a divisor is found, ensuring efficiency. If no divisors are found (i.e., `n` is prime), the function returns 1.