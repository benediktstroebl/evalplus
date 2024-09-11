```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the sum.
    
    Returns:
        int: The sum of numbers from 1 to n.
    """
    # Use the formula for the sum of an arithmetic series to calculate the sum
    return n * (n + 1) // 2


# Test the function
print(sum_to_n(30))
print(sum_to_n(100))
print(sum_to_n(5))
print(sum_to_n(10))
print(sum_to_n(1))
```

In this script, the `sum_to_n` function uses the formula for the sum of an arithmetic series, `n * (n + 1) / 2`, to calculate the sum of numbers from 1 to `n`. This formula is more efficient than using a loop to iterate over each number, especially for large values of `n`.