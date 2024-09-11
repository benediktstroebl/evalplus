```python
def sum_to_n(n: int) -> int:
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
        n (int): The last number in the sequence.
    
    Returns:
        int: The sum of numbers from 1 to n.
    """
    # We can use the formula for the sum of an arithmetic series to calculate the sum
    # The formula is n * (n + 1) / 2
    return n * (n + 1) // 2

# Test the function with given examples
print(sum_to_n(30))  # Should print 465
print(sum_to_n(100))  # Should print 5050
print(sum_to_n(5))  # Should print 15
print(sum_to_n(10))  # Should print 55
print(sum_to_n(1))  # Should print 1
```

This script defines a function `sum_to_n` that takes an integer `n` as input and returns the sum of numbers from 1 to `n`. It then tests the function with the given examples. The `//` operator is used for integer division to ensure the result is an integer.

Note: This function uses the formula `n * (n + 1) / 2` to calculate the sum, which has a time complexity of O(1), making it more efficient than a naive approach that sums the numbers from 1 to `n` individually, which would have a time complexity of O(n).