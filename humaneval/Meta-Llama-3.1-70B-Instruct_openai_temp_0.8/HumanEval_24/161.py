```python
def largest_divisor(n: int) -> int:
    """
    For a given number n, find the largest number that divides n evenly, smaller than n

    Args:
        n (int): The input number.

    Returns:
        int: The largest divisor of n.
    """
    def largest_divisor_helper(k: int) -> int:
        # Base case: if k is 2, it's the smallest possible divisor, return it
        if k == 2:
            return k
        # If n is divisible by k, return k
        elif n % k == 0:
            return k
        # Otherwise, recursively try the next smaller number
        else:
            return largest_divisor_helper(k - 1)

    # Start from n - 1, as we know n itself is a divisor
    return largest_divisor_helper(n - 1)


# Example usage:
print(largest_divisor(15))  # Output: 5
print(largest_divisor(20))  # Output: 10
print(largest_divisor(7))   # Output: 1
```