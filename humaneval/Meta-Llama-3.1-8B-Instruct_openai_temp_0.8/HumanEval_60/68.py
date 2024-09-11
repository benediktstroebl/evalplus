```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the sum.
    
    Returns:
        int: The sum of numbers from 1 to n.
    
    Examples:
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
    return sum(range(1, n + 1))

# Test the function
print(sum_to_n(30))  # Should print 465
print(sum_to_n(100))  # Should print 5050
print(sum_to_n(5))  # Should print 15
print(sum_to_n(10))  # Should print 55
print(sum_to_n(1))  # Should print 1
```

Alternatively, you can use the formula for the sum of an arithmetic series, which is `n * (n + 1) / 2`, to make the function more efficient:

```python
def sum_to_n(n: int):
    """
    This function calculates the sum of numbers from 1 to n.
    
    Args:
        n (int): The upper limit of the sum.
    
    Returns:
        int: The sum of numbers from 1 to n.
    
    Examples:
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
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # Should print 465
print(sum_to_n(100))  # Should print 5050
print(sum_to_n(5))  # Should print 15
print(sum_to_n(10))  # Should print 55
print(sum_to_n(1))  # Should print 1
```

This version of the function avoids the need to create a range object and sum all the numbers in it, making it more efficient for large values of `n`.