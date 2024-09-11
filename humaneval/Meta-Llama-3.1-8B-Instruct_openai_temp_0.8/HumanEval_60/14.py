```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    # Use the formula for the sum of an arithmetic series: n * (n + 1) / 2
    return n * (n + 1) // 2

# Test cases
print(sum_to_n(30))   # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))    # Expected output: 15
print(sum_to_n(10))   # Expected output: 55
print(sum_to_n(1))    # Expected output: 1
```

This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. The function uses the formula for the sum of an arithmetic series: `n * (n + 1) / 2`. The result is then printed for the specified test cases. 

Note: The `//` operator is used for integer division in Python 3, which means it returns the largest possible integer less than or equal to the result. This is why it's used instead of the `/` operator.