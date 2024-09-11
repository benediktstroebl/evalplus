```python
def sum_to_n(n: int) -> int:
    """
    This function sums numbers from 1 to n.

    Args:
        n (int): The upper limit for the sum.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    # Use the formula for the sum of an arithmetic series: n*(n+1)/2
    return n * (n + 1) // 2

# Test cases
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines a function `sum_to_n` that uses the mathematical formula for the sum of an arithmetic series to efficiently calculate the sum of numbers from 1 to `n`. The script then includes test cases to demonstrate the function's correctness.