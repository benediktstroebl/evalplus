```python
def sum_to_n(n: int):
    """
    This function calculates the sum of all numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the range for which the sum is calculated.
    
    Returns:
        int: The sum of all numbers from 1 to n.
    """
    # Use the formula for the sum of an arithmetic series: n * (n + 1) / 2
    # This is more efficient than using a loop to calculate the sum
    return n * (n + 1) // 2

# Test the function with the provided examples
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of all numbers from 1 to `n`. It uses the mathematical formula for the sum of an arithmetic series, which is more efficient than using a loop to calculate the sum. The script then tests the function with the provided examples to demonstrate that it works correctly.