```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.

    Args:
    n (int): The upper limit of the sum.

    Returns:
    int: The sum of numbers from 1 to n.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer.")
    
    # Calculate the sum using the formula for the sum of an arithmetic series
    # The formula is n * (a1 + an) / 2, where n is the number of terms, a1 is the first term, and an is the last term
    # In this case, a1 = 1 and an = n, so the formula simplifies to n * (1 + n) / 2
    sum_n = n * (n + 1) // 2
    
    return sum_n

# Test the function
print(sum_to_n(30))  # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))  # Expected output: 15
print(sum_to_n(10))  # Expected output: 55
print(sum_to_n(1))  # Expected output: 1
```

This script defines a function `sum_to_n(n)` that calculates the sum of numbers from 1 to `n` using the formula for the sum of an arithmetic series. The function takes an integer `n` as input and returns the sum. The script also includes test cases to demonstrate the function's behavior. 

Please note that this function uses integer division (`//`) to ensure that the result is an integer, even if `n` is large.