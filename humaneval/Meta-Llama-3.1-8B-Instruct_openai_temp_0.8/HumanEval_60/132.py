```python
def sum_to_n(n: int):
    """
    This function sums numbers from 1 to n.
    
    Args:
    n (int): The upper limit of the sum.
    
    Returns:
    int: The sum of numbers from 1 to n.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    
    # Calculate the sum using the formula n*(n+1)//2
    return n * (n + 1) // 2

# Test cases
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines the `sum_to_n` function, which takes an integer `n` as input and returns the sum of numbers from 1 to `n`. It includes type checking and input validation to handle invalid inputs. The function uses the formula `n*(n+1)//2` to calculate the sum efficiently, which is derived from the arithmetic progression sum formula. The test cases at the end demonstrate the function's correctness.