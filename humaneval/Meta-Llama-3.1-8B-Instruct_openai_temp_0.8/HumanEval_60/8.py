```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n using the formula n*(n+1)/2.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    return n * (n + 1) // 2

# Test cases
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n` using the formula `n*(n+1)/2`. The test cases are included at the end of the script to verify the function's correctness.