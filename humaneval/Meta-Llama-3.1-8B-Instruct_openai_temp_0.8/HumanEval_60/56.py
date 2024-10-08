```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    # The formula to calculate the sum of numbers from 1 to n is n*(n+1)/2
    return n * (n + 1) // 2

# Test cases
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function uses the mathematical formula `n*(n+1)/2` to calculate the sum, which is more efficient than iterating over all the numbers from 1 to `n`. The script also includes test cases to verify the correctness of the function.