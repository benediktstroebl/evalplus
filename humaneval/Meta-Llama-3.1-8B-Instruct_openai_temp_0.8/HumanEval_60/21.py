```python
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    # Use the math library's factorial function to calculate the sum
    import math

    # Calculate the sum using the formula n*(n+1)/2
    return n * (n + 1) // 2


# Test cases
print(sum_to_n(30))  # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))  # Expected output: 15
print(sum_to_n(10))  # Expected output: 55
print(sum_to_n(1))  # Expected output: 1
```

This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. It uses the mathematical formula `n*(n+1)/2` to calculate the sum, which is more efficient than iterating over the numbers from 1 to `n`. The script also includes test cases to verify the correctness of the function.