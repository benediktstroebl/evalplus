```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Args:
    n (int): The upper limit of the sum.
    
    Returns:
    int: The sum of numbers from 1 to n.
    
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    # Using the mathematical formula n*(n+1)/2 to calculate the sum
    return n * (n + 1) // 2

# Example usage
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This script defines a function `sum_to_n` that calculates the sum of numbers from 1 to `n`. The formula `n*(n+1)/2` is used to calculate the sum in constant time, making it more efficient than a simple loop. The example usage at the end shows how to use this function to calculate the sum for different values of `n`.