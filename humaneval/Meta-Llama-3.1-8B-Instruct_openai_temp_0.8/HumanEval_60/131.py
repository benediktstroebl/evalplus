```python
def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.

    Args:
        n (int): The upper limit of the sum.

    Returns:
        int: The sum of numbers from 1 to n.
    """
    # Use the formula for the sum of an arithmetic series: n*(n+1)/2
    # This is more efficient than using a for loop to iterate over the numbers
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))   # Expected output: 465
print(sum_to_n(100))  # Expected output: 5050
print(sum_to_n(5))    # Expected output: 15
print(sum_to_n(10))   # Expected output: 55
print(sum_to_n(1))    # Expected output: 1
```

This script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n`. It uses the formula for the sum of an arithmetic series, which is more efficient than using a for loop to iterate over the numbers. The function is then tested with some example inputs.