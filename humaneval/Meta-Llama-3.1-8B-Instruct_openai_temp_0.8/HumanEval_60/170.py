```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
    n (int): The upper limit for the sum.
    
    Returns:
    int: The sum of numbers from 1 to n.
    """
    # The formula to calculate the sum of numbers from 1 to n is n*(n+1)/2
    # We use this formula to calculate the sum directly instead of using a loop
    sum_of_numbers = n * (n + 1) // 2
    
    return sum_of_numbers

# Test the function
print(sum_to_n(30))   # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))    # Output: 15
print(sum_to_n(10))   # Output: 55
print(sum_to_n(1))    # Output: 1
```

This script defines a function `sum_to_n` that calculates the sum of numbers from 1 to n using the mathematical formula `n*(n+1)/2`. This formula is more efficient than using a loop to calculate the sum, especially for large values of n. The function is then tested with the provided input values.