```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n using the formula n*(n+1)/2.
    
    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    # Check if n is a non-negative integer
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    # Calculate the sum using the formula n*(n+1)/2
    total_sum = n * (n + 1) // 2
    
    return total_sum

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))    # Output: 15
print(sum_to_n(10))   # Output: 55
print(sum_to_n(1))    # Output: 1
```

This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function uses the mathematical formula `n*(n+1)/2` to calculate the sum, which is more efficient than using a loop to add up the numbers. The script also includes test cases to verify that the function works correctly.