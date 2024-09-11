```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Args:
    n (int): The upper limit of the series.

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
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

Alternatively, you can use the formula for the sum of an arithmetic series to improve the performance of the function:

```python
def sum_to_n(n: int):
    """
    sum_to_n is a function that sums numbers from 1 to n.
    
    Args:
    n (int): The upper limit of the series.

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
    return n * (n + 1) // 2

# Test the function
print(sum_to_n(30))  # Output: 465
print(sum_to_n(100))  # Output: 5050
print(sum_to_n(5))  # Output: 15
print(sum_to_n(10))  # Output: 55
print(sum_to_n(1))  # Output: 1
```

This version of the function uses the formula for the sum of an arithmetic series, which is `n * (n + 1) / 2`, where `n` is the number of terms in the series. This formula is more efficient than the original loop-based implementation.